"""定义learning_logs的URL模式"""

from django.urls import path, re_path
from django.conf.urls.static import static
from django.conf import settings

from . import views


# 命名空间
app_name = 'films'


# 注意path于re_path的用法区别
# path 用于不含参数方法的URL映射
# re_path 用于含参数方法的URL映射

urlpatterns = [
	# 显示所有的主题
	path('index/', views.index, name='index'),

	path('like/', views.like, name='like'),

	re_path('single/(?P<film_id>\d+)/', views.single, name='single'),
	re_path('comment/(?P<film_id>\d+)/', views.comment, name='comment'),
	re_path('movie/(?P<film_id>\d+)/', views.movie, name='movie'),

	path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('quit/', views.quit, name='quit'),
    path('person/', views.person, name='person')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
