"""定义learning_logs的URL模式"""

from django.urls import path, re_path


from . import views

#命名空间
app_name = 'small_tools'


#注意path于re_path的用法区别
#path 用于不含参数方法的URL映射
#re_path 用于含参数方法的URL映射

urlpatterns = [
    #小工具首页
	path('showTools/', views.showTools, name='showTools'),

    #snmp mib代码自动生成工具
	path('mibToCode/', views.mibToCode, name='mibToCode'),
]
