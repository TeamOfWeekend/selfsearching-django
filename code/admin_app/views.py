from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from django.contrib.auth.decorators import login_required


# Create your views here.

def index(request):
	"""学习笔记的首页"""
	return render(request, 'admin_app/index.html')


	
			
