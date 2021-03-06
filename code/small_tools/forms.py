from django import forms
from django.forms import widgets
from django.db import models

class AlgoStringForm(forms.Form):
    #字符串算法名称，暂时屏蔽，以后学习
    # algoName = forms.ChoiceField(
    #     label = '请选择一个算法',
    #     #初始值
    #     initial = '请选择一个算法',
    #     #选项
    #     choices = (),
    #     #是否必填
    #     required = True,
    #     #select添加属性
    #     widget = widgets.Select(attrs={
    #         "class" : "form-control",
    #         "id" : "algoSelect",
    #         "style" : "font-size:11pt"
    #     }),
    #     help_text = None,
    # )
    # #
    # def __init__(self, *args, **kwargs):
    #     super(AlgoStringForm, self).__init__(*args, **kwargs)
    #     #self.fields['algoName'].choices =
    strInput = forms.CharField(min_length = 10,
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



class AlgoRegixForm(forms.Form):
    """正则表达式小工具页面"""
    fileUpload = forms.FileField(required=False,
                                 widget = widgets.FileInput(attrs={
                                     'type': 'file',
                                     'id':'fileUpload',
                                     'accept': "text/plain, application/msword",
                                 }))
    strInput = forms.CharField(required=False,
                               widget = widgets.Textarea(attrs={
                                   'class': 'form-control',
                                   'id': 'strInput',
                                   'rows': '3',
                                   'style': 'background:#FFFFFF; color:#000000; font-size:11pt',
                                   'placeholder': '请输入一个字符串',
                               }))
    regixInput = forms.CharField(required=False,
                              widget = widgets.Textarea(attrs={
                                   'class':'form-control',
                                   'id':'regixInput',
                                   'rows':'2',
                                   'placeholder': '请输入待查找内容',
                               }))
    strOutput = forms.CharField(required=False,
                                widget = widgets.Textarea(attrs={
                                   'class':'form-control',
                                   'id':'strOutput',
                                   'rows':'10',
                                   'style':'background:#DCDCDC; color:#000000; font-size:9pt',
                                   'placeholder':'等待输出',
                                   'readonly': True
                               }))
    # def __init__(self, *args, **kwargs):
    #     super(AlgoRegixForm, self).__init__(*args, **kwargs)
    #     #self.fields['strOutput'] = models.Classes.objects.values_list['strOutput']

