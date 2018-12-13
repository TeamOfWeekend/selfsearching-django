#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author  : Leo
@Connect : lipf0627@163.com
@File    : forms.py
@site    :
@Time    : 2018/11/21 23:03
@Software: PyCharm Community Edition
"""

from django import forms
from .models import Film


class FilmForm(forms.ModelForm):
	"""大学表单"""
	class Meta:
		model = Film
		fields = ['name', 'description']
		labels = {'description': ''}


