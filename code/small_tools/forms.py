from django import forms
from django.forms import widgets

class AlgoStringForm(forms.Form):
    #字符串算法名称
    algoName = forms.ChoiceField(
        label = '请选择一个算法',
        #初始值
        initial = None,
        #选项
        choices = (),
        #是否必填
        required = True,
        #select添加属性
        widget = widgets.Select(attrs={
            "class" : "form-control",
            "id" : "algoSelect",
            "style" : "font-size:11pt"
        }),
        help_text = None,
    )





