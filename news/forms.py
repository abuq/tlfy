# -*-coding:utf-8 -*-
from django import forms

class NewsForm(forms.Form):
    title = forms.CharField(max_length = 40, label = '新闻标题')
    content = forms.CharField(max_length = 100000, widget = forms.Textarea, label
            = '新闻正文')

class PictureForm(forms.Form):
    file = forms.FileField(required = False)
