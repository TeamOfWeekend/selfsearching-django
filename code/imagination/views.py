from django.shortcuts import render

from .forms import CollegeEntryForm, CollegeForm, AcademyForm, MajorForm, GradeForm
from .collegeInfo.run import get_all_colleges_info, get_college_info, get_academy_info,\
    get_major_info, get_grade_info, get_class_info, get_teacher_info, get_student_info

# Create your views here.

def showIndex(request):
    return render(request, 'imagination/showIndex.html')


def collegeEntry(request):
    collegeEntryForm = CollegeEntryForm()
    # 生成学校信息列表，添加到学校选项中
    choice_list = []
    colleges_info = get_all_colleges_info()
    for college_name in colleges_info['colleges_name']:
        choice_list.append([college_name, college_name])
    collegeEntryForm.collegeChoiceSet(choice_list)
    return render(request, 'imagination/collegeEntry.html', {'collegeEntryForm': collegeEntryForm})


def collegeInfo(request):
    collegeForm = CollegeForm()
    choice_list = []

    if request.method == 'POST':
        college_name = request.POST['college_name']
        college_info = get_college_info(college_name)
        for academy_name in college_info['academies_name']:
            choice_list.append([academy_name, academy_name])
        collegeForm.academyChoiceSet(choice_list)

    return render(request, 'imagination/collegeInfo.html', {'collegeForm': collegeForm, 'college': college_info})


def academyInfo(request):
    global gCollege, gAcademy
    if request.method == 'POST':
        academy_name = request.POST['academy_name']
        academy_info = gCollege.academies[academy_name]

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



