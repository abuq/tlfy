# -*-coding:utf-8 -*-
from django import forms

class NoticeForm(forms.Form):
    content = forms.CharField(max_length = 200, widget =
            forms.Textarea(attrs={'cols':'40','rows':'10','maxlength':'200',
                }), label = '公告内容(200字以内)')
