# -*- coding:utf-8 -*-
from django import forms
from user_profile.models import UserProfile
from django.forms.widgets import CheckboxSelectMultiple

class SendMessageForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(SendMessageForm, self).__init__(*args, **kwargs)
        self.fields['receivers'] = forms.MultipleChoiceField(choices=[ (u.get_id(),
                    u.get_name()) for u in UserProfile.objects.all()], label =
                '收信人', required = True, widget = CheckboxSelectMultiple)
    title = forms.CharField(max_length = 50, label = '标题')
    content = forms.CharField(max_length = 100000, widget = forms.Textarea, label = '内容')
    #docfile = forms.FileField(label = '选择一个附件', help_text =
    #        '文件应小于20M', required = False)

