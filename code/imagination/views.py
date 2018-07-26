from django.shortcuts import render

from .collegeInfo import imCollege


# Create your views here.


def showIndex(request):
    college = imCollege.ImCollege()
    college.createRandomAttrs()
    return render(request, 'imagination/showIndex.html')


def collegeInfo(request):
    return render(request, 'imagination/collegeInfo.html')