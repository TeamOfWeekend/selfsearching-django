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

gCollege = None
gAcademy = None
gMajor = None
gGrade = None
gClass = None

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
        global gCollege
        gCollege = getCollege(collegeName)
        return render(request, 'imagination/collegeInfo.html', {'collegeForm': collegeForm, 'college': gCollege})


def academyInfo(request):
    global gCollege, gAcademy
    if request.method == 'POST':
        academyName = request.POST['academyName']
        gAcademy = gCollege.academies[academyName]
        academyForm = AcademyForm()
        choice_list = []
        for key in gAcademy.majors.keys():
            choice_list.append([key, key])
        academyForm.majorChoiceSet(choice_list)

        context = {'academyForm': academyForm, 'academy': gAcademy, 'college': gCollege}
        return render(request, 'imagination/academyInfo.html', context)


def majorInfo(request):
    global gCollege, gAcademy, gMajor
    if request.method == 'POST':
        majorName = request.POST['majorName']
        gMajor = gAcademy.majors[majorName]
        print(gAcademy.majors)
        print(gMajor.name)
        majorForm = MajorForm()
        choice_list = []
        for grade in range(1, len(gMajor.grades) + 1):
            choice_list.append([grade, grade])
        majorForm.gradeChoiceSet(choice_list)

        context = {'majorForm': majorForm, 'majorName': majorName,
                   'major': gMajor, 'academy': gAcademy, 'college': gCollege}
        return render(request, 'imagination/majorInfo.html', context)


def gradeInfo(request):
    global gCollege, gAcademy, gMajor, gGrade
    if request.method == 'POST':
        gradeForm = GradeForm()
        gradeId = request.POST['gradeId']
        gGrade.id = gMajor.grades[gradeId-1]
        context = {'gradeForm': gradeForm, 'grade': gGrade,
                   'major': gMajor, 'academy': gAcademy, 'college': gCollege}
        return render(request, 'imagination/gradeInfo.html', {'gradeForm': gradeForm, 'grade': grade})


def classInfo(request):
    classs = ImClass()
    classs.id = 1
    return render(request, 'imagination/classInfo.html', {'classs': classs})


def studentInfo(request):
    student = ImStudent()
    student.name = '小红'
    return render(request, 'imagination/studentInfo.html', {'student': student})


