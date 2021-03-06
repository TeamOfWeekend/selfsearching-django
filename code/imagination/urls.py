"""定义learning_logs的URL模式"""

from django.urls import path, re_path
# from django.views.decorators.csrf import csrf_exempt

from . import views

# 命名空间
app_name = 'imagination'


# 注意path于re_path的用法区别
# path 用于不含参数方法的URL映射
# re_path 用于含参数方法的URL映射

urlpatterns = [
    # 小工具首页
	path('showIndex/', views.showIndex, name='showIndex'),
	# 学校入口页面
	path('collegeEntry/', views.collegeEntry, name='collegeEntry'),
	# 学校信息页面
	path('collegeInfo/', views.collegeInfo, name='collegeInfo'),
	path('academyInfo/', views.academyInfo, name='academyInfo'),
	path('majorInfo/', views.majorInfo, name='majorInfo'),
	path('gradeInfo/', views.gradeInfo, name='gradeInfo'),
	path('classInfo/', views.classInfo, name='classInfo'),
	re_path('studentInfo/(?P<student_id>\d+)/', views.studentInfo, name='studentInfo'),
	re_path('teacherInfo/(?P<teacher_id>\d+)/', views.teacherInfo, name='teacherInfo'),
]
