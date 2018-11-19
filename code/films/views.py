from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

# 注释掉该修饰器，否则用户未登录时不能进行跳转
@login_required
def films(request):
    """显示所有的主题"""
    if request.user.is_authenticated:
        # 从数据库中查找某用户的所有主题，并按添加日期降序排列
		# topics = Films.objects.filter(owner=request.user).order_by('date_added')
		# context = {'topics': topics}
		# return render(request, 'films/films.html', context)
        return render(request, 'films/films.html')
    else:
        return render(request, 'users/login.html')
