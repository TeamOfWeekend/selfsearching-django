from django.shortcuts import render
from django.contrib.auth.decorators import login_required

import os
import sys
import platform
# import filetype

from .models import Film
from .forms import FilmForm

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
def films(request):
    """显示所有的主题"""
    global films_path
    if request.user.is_authenticated:
        films_list = []
        films_dir_list = os.listdir(films_path)     # 获取文件夹下所有的目录与文件
        print('films_list ------------------ %d' % len(films_dir_list))
        for i in range(len(films_dir_list)):
            film_folder = os.path.join(films_path, films_dir_list[i])
            print('********************************* film_folder = %s' % film_folder)
            if os.path.isdir(film_folder):
                files_list = os.listdir(film_folder)      # 获取所有文件
                if len(files_list) == 2:
                    film_description = ''
                    film_name = ''
                    files_valid = 0   # 标识两个文件：视频文件、文本文件
                    print(files_list)

                    for j in range(len(files_list)):
                        if is_video(files_list[j]):   # 文件为视频文件
                            film_name = os.path.splitext(files_list[j])[0]
                            film_path = os.path.join(film_folder, film_name)
                            files_valid |= (0x01 << 0)
                        elif os.path.splitext(files_list[j])[1] == '.txt':  # 文本文件
                            print(files_list[j])
                            txt_path = os.path.join(film_folder, files_list[j])
                            with open(txt_path, 'r', encoding='utf-8') as f:
                                for line in f.readlines():
                                    film_description += line.rstrip('\n')
                            files_valid |= (0x01 << 1)

                    if files_valid == 0x03:
                        film_form = FilmForm()
                        film_form.Meta.model.name = film_name
                        film_form.Meta.model.description = film_description
                        film_form.Meta.model.id = (i + 1)
                        films_list.append(film_form)
                    else:
                        pass

                else:
                    pass
        context = {'films_list': films_list}
        print('---------------------------%d' % len(films_list))
        for i in range(len(films_list)):
            print(id(films_list[i]))
            print(films_list[i].Meta.model.name)
            print(films_list[i].Meta.model.id)
            print(films_list[i].Meta.model.description)
        print('---------------------------')
        return render(request, 'films/films.html', context)
    else:
        return render(request, 'users/login.html')


@login_required
def film(request, film_id):
    """
    显示film
    :param request:
    :return:
    """
    if request.user.is_authenticated:
        topics = []
        # 从数据库中查找某用户的所有主题，并按添加日期降序排列
        # topics = Films.objects.filter(owner=request.user).order_by('date_added')
        # context = {'topics': topics}
        # return render(request, 'films/films.html', context)
        film = Film.objects.get(id=film_id)
        context = {'film': film}
        return render(request, 'films/film.html', context)
    else:
        return render(request, 'users/login.html')


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
