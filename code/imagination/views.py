from django.shortcuts import render

from .collegeInfo import imCollege

from .forms import CollegeForm

# Create your views here.


def showIndex(request):
    college = imCollege.ImCollege()
    college.createRandomAttrs()
    return render(request, 'imagination/showIndex.html')


def collegeInfo(request):
    # collegeForm = CollegeForm.objects.get(name='郑州大学')
    collegeForm = CollegeForm()
    collegeForm.name = '郑州大学'
    return render(request, 'imagination/collegeInfo.html', {'collegeForm': collegeForm})
