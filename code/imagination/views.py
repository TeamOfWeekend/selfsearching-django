from django.shortcuts import render

from .calcCollegeInfo import imCollege


# Create your views here.


def showIndex(request):
    college = imCollege.ImCollege()
    college.createRandomAttrs()
    return render(request, 'imagination/showIndex.html')


def inputCollegeInfo(request):
    return render(request, 'imagination/inputCollegeInfo.html')