from django import forms
from django.forms import widgets
from django.db import models

class CollegeForm(forms.Form):
    """大学表单"""
    collegeName = forms.CharField(min_length = 10,
                               strip = True,
                               error_messages = {
                                   'required':'该字段不能为空',
                                   'min_length':'字符串长度不能小于1'
                               },
                               widget = widgets.Textarea(attrs={
                                   'class':'form-control',
                                   'id':'strInput',
                                   'rows':'6',
                                   'style':'background:#FFFFFF; color:#000000; font-size:11pt',
                                   'placeholder':'请输入一个字符串',
                               }))
    # strOutput = forms.CharField(min_length = 1,
    #                            strip = True,
    #                            error_messages = None,
    #                            widget = widgets.Textarea(attrs={
    #                                'class':'form-control',
    #                                'id':'strOutput',
    #                                'rows':'6',
    #                                'style':'background:#DCDCDC; color:#000000; font-size:11pt',
    #                                'placeholder':'等待计算结果',
    #                                'readonly':'true'
    #                            }))





