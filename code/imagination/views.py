from django.shortcuts import render

from .collegeInfo import imCollege

from .forms import CollegeEntryForm, CollegeForm
from .collegeInfo.imTypes import AcademyEnum

# Create your views here.


def showIndex(request):
    college = imCollege.ImCollege()
    college.createRandomAttrs()
    return render(request, 'imagination/showIndex.html')


def collegeEntry(request):
    # collegeForm = CollegeForm.objects.get(name='郑州大学')
    collegeForm = CollegeEntryForm()
    collegeForm.name = '郑州大学'
    return render(request, 'imagination/collegeEntry.html', {'collegeForm': collegeForm})


def collegeInfo(request):
    collegeForm = CollegeForm()
    collegeName = '郑州大学'

    choice_list = []
    for item in AcademyEnum:
        choice_list.append([item.value, item.name])
    collegeForm.academyChoiceSet(choice_list)

    return render(request, 'imagination/collegeInfo.html', {'collegeForm': collegeForm, 'collegeName': collegeName})
