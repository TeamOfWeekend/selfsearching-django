from django.shortcuts import render

# Create your views here.


def showIndex(request):
    return render(request, 'imagination/showIndex.html')


def inputCollegeInfo(request):
    return render(request, 'imagination/inputCollegeInfo.html')