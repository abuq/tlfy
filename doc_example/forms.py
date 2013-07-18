# -*- coding: utf-8 -*-
from django import forms

class DocExampleForm(forms.Form):
    title = forms.CharField(max_length = 60, label = '文书标题（30字以内）')
    docfile = forms.FileField(
        label='选择一个文件',
        help_text='文件应小于20M'
    )
