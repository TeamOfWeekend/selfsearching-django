from django.shortcuts import render
from django.contrib.auth.decorators import login_required

import os
import sys
import platform
import json
import xml.etree.ElementTree as ET
import copy
# import filetype

from .models import Movie, Comment
# from .forms import FilmForm
from .lib.film import Film

# Create your views here.

# find current path  os what system we're on
# find films path
films_path = ''
if "Windows" == platform.system():
    # sys.path.append(os.path.abspath('.') + "\\libs")
    films_path = "static\\video"
else:
    # sys.path.append(os.path.abspath('.') + "/libs")
    films_path = "static/video"


# html_list = os.listdir('films\\templates\\films')
# print(html_list)
# video_list = os.listdir('static\\video')
# print(video_list)


# 注释掉该修饰器，否则用户未登录时不能进行跳转
@login_required
def show_films(request):
    """显示所有的主题"""
    if request.user.is_authenticated:
        films_list = get_all_films()

        context = {'films_list': films_list}
        return render(request, 'films/show_films.html', context)
    else:
        return render(request, 'users/login.html')


@login_required
def show_film(request, film_id):
    """
    显示film
    :param request:
    :return:
    """
    # print(request.META['wsgi.url_scheme'])        # http
    # print(request.META['HTTP_HOST'])              # 127.0.0.1:8000
    if request.user.is_authenticated:
        film = get_all_films()[int(film_id) - 1]
        context = {'film': film}
        film.url = request.META['wsgi.url_scheme'] + '://' + request.META['HTTP_HOST'] + '/' + film.url
        print(film.url)
        return render(request, 'films/show_film.html', context)
        # return render(request, 'films/base.html')
        # return render(request, 'films/movie.html')
    else:
        return render(request, 'users/login.html')


# def get_all_films():
#     global films_path
#     films_list = []
#     films_dir_list = os.listdir(films_path)  # 获取文件夹下所有的目录与文件
#     # print('films_list ------------------ %d' % len(films_dir_list))
#     for i in range(len(films_dir_list)):
#         film_folder = os.path.join(films_path, films_dir_list[i])
#         # print('********************************* film_folder = %s' % film_folder)
#         if os.path.isdir(film_folder):
#             files_list = os.listdir(film_folder)  # 获取所有文件
#             if len(files_list) == 2:
#                 film_description = ''
#                 film_name = ''
#                 film_path = ''
#                 files_valid = 0  # 标识两个文件：视频文件、文本文件
#                 # print(files_list)
#
#                 for j in range(len(files_list)):
#                     if is_video(files_list[j]):  # 文件为视频文件
#                         # film_name = os.path.splitext(files_list[j])[0]
#                         film_name = files_list[j]
#                         film_path = os.path.join(film_folder, film_name)
#                         files_valid |= (0x01 << 0)
#                     elif os.path.splitext(files_list[j])[1] == '.txt':  # 文本文件
#                         print(files_list[j])
#                         txt_path = os.path.join(film_folder, files_list[j])
#                         with open(txt_path, 'r', encoding='utf-8') as f:
#                             for line in f.readlines():
#                                 film_description += line.rstrip('\n')
#                         files_valid |= (0x01 << 1)
#
#                 if files_valid == 0x03:
#                     film_form = Film()
#                     film_form.name = film_name
#                     film_form.description = film_description
#                     film_form.num = (i + 1)
#                     film_form.url = film_path
#                     films_list.append(copy.deepcopy(film_form))
#                 else:
#                     pass
#             else:
#                 pass
#     return films_list


def get_all_films():
    """
    从movies.json或movies.xml文件获取全部电影信息
    :return:
    """
    global films_path
    MOVIES_JSON = 'movies.json'
    MOVIES_XML = 'movies.xml'
    films_list = []
    files_name_all = os.listdir(films_path)  # 获取文件夹下所有的目录与文件
    for file_name in files_name_all:
        file_dir = os.path.join(films_path, file_name)
        print(file_name)
        # if file_name is MOVIES_JSON:
        #     with open(file_dir, 'r', encoding='utf-8') as f:
        #         dict_load = json.load(f)
        #         print(dict_load)
        if file_name == MOVIES_XML:
            tree = ET.parse(file_dir)
            # 获取所有movie
            movies_list = tree.findall('movie')
            # print(movies_list)
            for movie in movies_list:
                print(movie.find('name').text)


# 详情页
@login_required
def single(request, mid):
    key = request.COOKIES.get('usernameKey')
    usernameKey = request.session.get(key, 0)

    token = request.COOKIES.get('userToken')

    single_movie = Movie.objects.get(id=mid)

    try:
        currentuser = User.objects.get(token=token)
    except User.DoesNotExist as e:
        currentuser = None

    # print(single_movie.like.all())  # 返回当前电影对应的收藏用户名称
    if currentuser != None:  # 当前用户已登陆
        if currentuser in single_movie.like.all():  # 当前登陆用户已经收藏了本电影
            is_like = 1
        else:  # 当前用户没有收藏此电影
            is_like = 0
    else:
        is_like = 3

    single_movie.single_link = 'https://img3.doubanio.com/view/photo/s_ratio_poster/public/' + \
                               str(single_movie.cover_link).split('_')[0] + '.webp'
    if single_movie.single_link.count('.webp') > 1:
        single_movie.single_link = single_movie.single_link[: len(single_movie.single_link) - 5]

    # 侧边栏推荐
    side_recommend = Movie.objects.order_by('-mark')[ : 3]
    for s in side_recommend:
        s.new_link = 'https://img3.doubanio.com/view/photo/s_ratio_poster/public/' + str(s.cover_link).split('_')[0] + '.webp'
        if s.new_link.count('.webp') > 1:
            s.new_link = s.new_link[ : len(s.new_link) - 5]

        s.like_count = len(s.like.all())


    # 获取评论
    try:
        comment_list = Comment.objects.filter(movie_id=mid)
    except Comment.DoesNotExist as e:
        comment_list = []
    comment_list_count = len(comment_list)  # 评论总数

    return render(request, 'single.html', {'movie':single_movie,
                                           'side_recommend':side_recommend,
                                           'username':usernameKey,
                                           'is_like':is_like,
                                           'comment_list':comment_list,
                                           'comment_list_count':comment_list_count,
                                           })


def is_video(file_name):
    """
    根据文件的后缀名判断是否为视频文件
    :param file_name:
    :return:
    """
    video_names = ('.mp4', '.m4v', '.mkv', '.webm', '.mov'
                   '.avi', '.wmv', '.mpg', '.flv')
    extension_name = os.path.splitext(file_name)[1]
    if extension_name in video_names:
        return True
    else:
        return False
