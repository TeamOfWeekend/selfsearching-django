"""定义learning_logs的URL模式"""

from django.urls import path, re_path


from . import views

#命名空间
app_name = 'learning_logs'


#注意path于re_path的用法区别
#path 用于不含参数方法的URL映射
#re_path 用于含参数方法的URL映射

urlpatterns = [
	#显示所有的主题
	path('topics/', views.topics, name='topics'),

	#显示指定主题的细节
	re_path('topics/(?P<topic_id>\d+)/', views.topic, name='topic'),

	#用于添加新主题的网页
	path('new_topic/', views.new_topic, name='new_topic'),

	#用于添加新条目的页面
	re_path('new_entry/(?P<topic_id>\d+)/', views.new_entry, name='new_entry'),

	#用于编辑条目的页面
	re_path('edit_entry/(?P<entry_id>\d+)/', views.edit_entry, name='edit_entry'),
]
