from django.shortcuts import render
from django.http import HttpResponse

from .smallToolsSet import algoStringSet
import os
# Create your views here.


def showTools(request):
	"""学习笔记的首页"""
	return render(request, 'small_tools/showTools.html')


def mibToCode(request):
	"""学习笔记的首页"""
	return render(request, 'small_tools/mibToCode.html')


def algoString(request):
	"""获取并处理algoString.html数据"""
	if request.is_ajax():
		#algoName = request.GET['algoName']
		#print(algoName)
		strInput = request.GET['strInput']
		strOutput = algoStringSet.deleteRepeatedChars(strInput)
		return HttpResponse(strOutput)
	else:
		algoNames = algoStringSet.showAllStringAlgos()
		context = {'algoNames': algoNames}
		return render(request, 'small_tools/algoString.html', context)
