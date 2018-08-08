from django.shortcuts import render

from .collegeInfo import imCollege

from .forms import CollegeEntryForm, CollegeForm, AcademyForm, MajorForm, GradeForm
from .collegeInfo.imTypes import AcademyEnum
from .collegeInfo.imCollege import ImCollege
from .collegeInfo.imAcademy import ImAcademy
from .collegeInfo.imMajor import ImMajor
from .collegeInfo.imGrade import ImGrade
from .collegeInfo.imClass import ImClass
from .collegeInfo.imStudent import ImStudent

# Create your views here.


def showIndex(request):
    return render(request, 'imagination/showIndex.html')


def collegeEntry(request):
    # collegeForm = CollegeForm.objects.get(name='郑州大学')
    collegeForm = CollegeEntryForm()
    collegeForm.name = '郑州大学'
    return render(request, 'imagination/collegeEntry.html', {'collegeForm': collegeForm})


def collegeInfo(request):
    collegeForm = CollegeForm()
    college = imCollege.ImCollege()
    college.createRandomAttrs()
    # college.name = '郑州大学'
    print(college.name)
    print(type(college.name))
    college.id = 123
    college.address = '郑州高新区'
    college.area = 5000
    college.level = 1
    college.academyNum = 10

    choice_list = []
    for item in AcademyEnum:
        choice_list.append([item.value, item.name])
    collegeForm.academyChoiceSet(choice_list)

    return render(request, 'imagination/collegeInfo.html', {'collegeForm': collegeForm, 'college': college})


def academyInfo(request):
    academyForm = AcademyForm()
    academy = ImAcademy()
    academy.name = '电气工程学院'
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
