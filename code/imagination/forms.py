from django import forms
from django.forms import widgets

from .models import CollegeInfo


# Form 仅做表单数据验证
# ModelForm 做数据库与表单数据验证

class CollegeForm(forms.ModelForm):
    """大学表单"""
    class Meta:
        # 表单对应的模型
        model = CollegeInfo
        # 引入的模型的属性
        fields = ['name', 'collegeId', 'address', 'level', 'area', 'academyNum']
        # 配置上述属性的html属性
        widgets = {
            'name': forms.CharField(attrs={'class': "form-control",
                                           'id': "collegeName",
                                           'readonly': 'true'}),
            'collegeId': forms.IntegerField(attrs={'class': "form-control",
                                                   'id': "collegeId",
                                           'readonly': 'true'}),
        }



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





