from django.shortcuts import render

#import backEndCode

# Create your views here.


def showTools(request):
	"""学习笔记的首页"""
	return render(request, 'small_tools/showTools.html')


def mibToCode(request):
	"""学习笔记的首页"""
	return render(request, 'small_tools/mibToCode.html')


def algoString(request):
	"""获取并处理algoString.html数据"""
	return render(request, 'small_tools/algoString.html')
	if request.method == 'POST':
		# 获取前端数据
		# algoName = request.POST.get('algoName','')
		# strInput = request.POST.get('strInput', '')
		#进行数据处理
		# strOutput = strInput[:]
		# context = {'strOutput': strOutput}
		#return render(request, 'small_tools/algoString.html', context)
		return render(request, 'small_tools/algoString.html')
	else:
		return render(request, 'small_tools/algoString.html')


