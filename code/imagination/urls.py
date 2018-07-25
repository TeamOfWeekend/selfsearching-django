"""定义learning_logs的URL模式"""

from django.urls import path, re_path
from django.views.decorators.csrf import csrf_exempt

from . import views

#命名空间
app_name = 'imagination'


#注意path于re_path的用法区别
#path 用于不含参数方法的URL映射
#re_path 用于含参数方法的URL映射

urlpatterns = [
    #小工具首页
	path('showIndex/', views.showIndex, name='showIndex'),
	path('collegeInfo/', views.collegeInfo, name='collegeInfo'),
]
