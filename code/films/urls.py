"""定义learning_logs的URL模式"""

from django.urls import path, re_path

from . import views

#命名空间
app_name = 'films'


#注意path于re_path的用法区别
#path 用于不含参数方法的URL映射
#re_path 用于含参数方法的URL映射

urlpatterns = [
	#显示所有的主题
	path('films/', views.films, name='films'),

	re_path('films/(?P<film_id>d+)/', views.film, name='film'),

	#显示指定主题的细节
	# re_path('topics/(?P<topic_id>\d+)/', views.topic, name='topic'),
]
