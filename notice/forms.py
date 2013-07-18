# -*-coding:utf-8 -*-
from django import forms

class NoticeForm(forms.Form):
    content = forms.CharField(max_length = 200, widget = forms.Textarea, label =
            '公告内容(100字以内)')
