from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import os
import json

from .smallToolsSet import algoStringApi

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


@csrf_exempt
def algoRegix(request):
	"""正则表达式学习"""
	if request.is_ajax():
		print("postttttttttttttttttttttttttttttt")
		strInput = request.POST.get('strInput')
		print(strInput)
		fileUpload = request.FILES.get('fileUpload')
		if fileUpload:
			print('接收到了上传的文件')
		else:
			print('没有接收到上传的文件')
		strOutput = 'fdjksfjdlsfjlsdjf'
		# return render(request, 'small_tools/algoRegix.html', {'strOutput':strOutput})
		return HttpResponse(strOutput)
	else:
		print("gettttttttttttttttttttttttttttttt")
		return render(request, 'small_tools/algoRegix.html')
	# if request.method == 'GET':
	# 	img_list = models.Img.objects.all()
	# 	return render(request, 'upload.html', {'img_list': img_list})
	# elif request.method == "POST":
	# 	user = request.POST.get('user')
	# 	fafafa = request.POST.get('fafafa')
    #
	# 	obj = request.FILES.get('fafafa')
	# 	# print(obj.name,obj.size)  #读取文件名称和大小，返回后台
	# 	# print(user,fafafa)
	# 	file_path = os.path.join('static', 'upload', obj.name)
	# 	f = open(file_path, 'wb')
	# 	for chunk in obj.chunks():
	# 		f.write(chunk)
	# 	f.close()
	# 	models.Img.objects.create(path=file_path)
    #
	# 	ret = {'status': True, 'path': file_path}
	# 	return HttpResponse(json.dumps(ret))
