from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
# from django.urls import reverse

from .forms import AlgoRegixForm

from .smallToolsSet import algoStringApi
from .smallToolsSet import algoRegixApi
from .mathTools.random_walk import RandomWalk
from .mathTools.worldPopulation import WorldPopulationMap
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
		algoName = request.GET['algoSelect']
		strInput = request.GET['strInput']
		strOutput = algoStringApi.processString(algoName, strInput)
		return HttpResponse(strOutput)
	else:
		algoNames = algoStringApi.getAllStringAlgos()
		context = {'algoNames': algoNames}
		return render(request, 'small_tools/algoString.html', context)


#@csrf_exempt
def algoRegix(request):
	"""正则表达式学习"""
	if request.method != 'POST':
		form = AlgoRegixForm()
		return render(request, 'small_tools/algoRegix.html', {'form':form})
	else:
		strOutput = ''
		strInput = request.POST.get('strInput',None)
		regixInput = request.POST.get('regixInput', None)
		fileUpload = request.FILES.get('fileUpload', None)
		# print(strInput)
		# print(fileUpload)
		# print(regixInput)
		if fileUpload != None:
			strIn = str(fileUpload.read())
			strIn = strIn[2:(len(strIn) -2)]
			strOutput = algoRegixApi.findAllStringByRegix(regixInput, strIn)
		elif len(strInput):
			strOutput = algoRegixApi.findAllStringByRegix(regixInput, strInput)
		# with open(fileUpload.name, 'r') as f:
		# 	contents = f.read()
		# 	print(contents)
		# strOutput = 'Output tessssssssssst'

		randomWalk = RandomWalk()
		randomWalk.drawWalkMap()

		wm = WorldPopulationMap(2016)
		wm.draw_population_map()

		return HttpResponse(strOutput)

