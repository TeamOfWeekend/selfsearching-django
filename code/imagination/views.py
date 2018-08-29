from django.shortcuts import render

from .collegeInfo import imCollege

from .forms import CollegeEntryForm, CollegeForm, AcademyForm, MajorForm, GradeForm
from .collegeInfo.imTypes import CollegeEnum, AcademyEnum
from .collegeInfo.imStudent import ImStudent
from .main import getCollege

# Create your views here.


# 暂时使用该方法运行后台程序
# main()

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
    collegeForm = CollegeForm()
    choice_list = []
    for item in AcademyEnum:
        choice_list.append([item.name, item.name])
    collegeForm.academyChoiceSet(choice_list)
    global gCollege

    if request.method == 'POST':
        collegeName = request.POST['collegeName']
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

    majorForm = MajorForm()
    choice_list = []
    for grade in range(1, len(gMajor.grades) + 1):
        choice_list.append([grade, grade])
    majorForm.gradeChoiceSet(choice_list)
    context = {'majorForm': majorForm, 'major': gMajor,
               'academy': gAcademy, 'college': gCollege}
    return render(request, 'imagination/majorInfo.html', context)


def gradeInfo(request):
    global gCollege, gAcademy, gMajor, gGrade

    if request.method == 'POST':
        gradeId = int(request.POST['gradeId'])
        gGrade = gMajor.grades[gradeId-1]

    gradeForm = GradeForm()
    choice_list = []
    for classesId in range(1, len(gGrade.classes) + 1):
        choice_list.append([classesId, classesId])
    gradeForm.classChoiceSet(choice_list)

    context = {'gradeForm': gradeForm, 'grade': gGrade,
               'major': gMajor, 'academy': gAcademy, 'college': gCollege}
    return render(request, 'imagination/gradeInfo.html', context)


def classInfo(request):
    global gCollege, gAcademy, gMajor, gGrade, gClass
    if request.method == 'POST':
        # print(request.POST)
        classsId = int(request.POST['classId'])
        gClass = gGrade.classes[classsId-1]
    context = {'classs': gClass, 'grade': gGrade,
               'major': gMajor, 'academy': gAcademy, 'college': gCollege}
    return render(request, 'imagination/classInfo.html', context)


def studentInfo(request):
    student = ImStudent()
    student.name = '小红'
    return render(request, 'imagination/studentInfo.html', {'student': student})



