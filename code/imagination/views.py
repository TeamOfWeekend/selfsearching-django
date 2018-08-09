from django.shortcuts import render

from .collegeInfo import imCollege

from .forms import CollegeEntryForm, CollegeForm, AcademyForm, MajorForm, GradeForm
from .collegeInfo.imTypes import CollegeEnum, AcademyEnum, ACADEMY_MAJOR_DIR
from .collegeInfo.imCollege import ImCollege
from .collegeInfo.imAcademy import ImAcademy
from .collegeInfo.imMajor import ImMajor
from .collegeInfo.imGrade import ImGrade
from .collegeInfo.imClass import ImClass
from .collegeInfo.imStudent import ImStudent
from .main import main, getCollege

# Create your views here.


# 暂时使用该方法运行后台程序
main()
gCollege = ImCollege()

def showIndex(request):
    return render(request, 'imagination/showIndex.html')


def collegeEntry(request):
    collegeEntryForm = CollegeEntryForm()
    # 生成学校信息列表，添加到学校选项中
    choice_list = []
    for item in CollegeEnum:
        choice_list.append([item.name, item.name])
    collegeEntryForm.collegeChoiceSet(choice_list)
    return render(request, 'imagination/collegeEntry.html', {'collegeEntryForm': collegeEntryForm})


def collegeInfo(request):
    if request.method == 'POST':
        collegeName = request.POST['collegeName']

        collegeForm = CollegeForm()
        choice_list = []
        for item in AcademyEnum:
            choice_list.append([item.name, item.name])
        collegeForm.academyChoiceSet(choice_list)

        gCollege = getCollege(collegeName)

    return render(request, 'imagination/collegeInfo.html', {'collegeForm': collegeForm, 'college': gCollege})


def academyInfo(request):
    if request.method == 'POST':
        academyName = request.POST['academyName']

        academyForm = AcademyForm()
        choice_list = []
        for key in ACADEMY_MAJOR_DIR.keys():
            choice_list.append([key, key])
        academyForm.majorChoiceSet(choice_list)
        print(gCollege.name)
        print(gCollege.academies)

        academy = gCollege.academies[academyName]
    return render(request, 'imagination/academyInfo.html', {'academyForm': academyForm, 'academy': academy})


def majorInfo(request):
    majorForm = MajorForm()
    major = ImMajor()
    major.name = '电气工程学院'
    return render(request, 'imagination/majorInfo.html', {'majorForm': majorForm, 'major': major})


def gradeInfo(request):
    gradeForm = GradeForm()
    grade = ImGrade()
    grade.id = 1
    return render(request, 'imagination/gradeInfo.html', {'gradeForm': gradeForm, 'grade': grade})


def classInfo(request):
    classs = ImClass()
    classs.id = 1
    return render(request, 'imagination/classInfo.html', {'classs': classs})


def studentInfo(request):
    student = ImStudent()
    student.name = '小红'
    return render(request, 'imagination/studentInfo.html', {'student': student})


