from django.shortcuts import render

from .forms import CollegeEntryForm, CollegeForm, AcademyForm, MajorForm, GradeForm, ClassForm
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
    college_name = ''

    if request.method == 'POST':
        college_name = request.POST['college_name']

    college_info = get_college_info(college_name)
    for academy_name in college_info['academies_name']:
        choice_list.append([academy_name, academy_name])
    collegeForm.academyChoiceSet(choice_list)
    return render(request, 'imagination/collegeInfo.html', {'collegeForm': collegeForm, 'college': college_info})


def academyInfo(request):
    academyForm = AcademyForm()
    choice_list = []
    academy_name = ''

    if request.method == 'POST':
        academy_name = request.POST['academy_name']

    academy_info = get_academy_info(academy_name)
    for major_name in academy_info['majors_name']:
        choice_list.append([major_name, major_name])
    academyForm.majorChoiceSet(choice_list)

    context = {'academyForm': academyForm, 'academy': academy_info}
    return render(request, 'imagination/academyInfo.html', context)


def majorInfo(request):
    majorForm = MajorForm()
    choice_list = []
    major_name = ''

    if request.method == 'POST':
        major_name = request.POST['major_name']

    major_info = get_major_info(major_name)
    for grade_id in range(1, major_info['grades_num'] + 1):
        choice_list.append([grade_id, grade_id])
    majorForm.gradeChoiceSet(choice_list)
    context = {'majorForm': majorForm, 'major': major_info}
    return render(request, 'imagination/majorInfo.html', context)


def gradeInfo(request):
    gradeForm = GradeForm()
    choice_list = []
    grade_id = 0

    if request.method == 'POST':
        grade_id = int(request.POST['grade_id'])

    grade_info = get_grade_info(grade_id)
    for class_id in range(1, grade_info['classes_num'] + 1):
        choice_list.append([class_id, class_id])
    gradeForm.classChoiceSet(choice_list)

    context = {'gradeForm': gradeForm, 'grade': grade_info}
    return render(request, 'imagination/gradeInfo.html', context)


def classInfo(request):
    # classForm = ClassForm()
    class_id = 0
    if request.method == 'POST':
        class_id = int(request.POST['class_id'])
    class_info = get_class_info(class_id)
    # for student_info in class_info['students_info']:

    context = {'classs': class_info}
    return render(request, 'imagination/classInfo.html', context)


def studentInfo(request):
    student_id = 0
    if request.method == 'POST':
        student_id = int(request.POST['student_id'])
    student_info = get_student_info(student_id)
    context = {'classs': student_info}
    return render(request, 'imagination/classInfo.html', context)


def teacherInfo(request):
    teacher_name = ''
    if request.method == 'POST':
        teacher_name = int(request.POST['teacher_name'])
    teacher_info = get_student_info(teacher_name)
    context = {'classs': teacher_info}
    return render(request, 'imagination/classInfo.html', context)


