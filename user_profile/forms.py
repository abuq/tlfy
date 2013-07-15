# -*- coding:utf-8 -*-
from django import forms
from user_profile.models import UserProfile

class LoginForm(forms.Form):
    username = forms.CharField(max_length = 40, label='用户名')
    pwd = forms.CharField(max_length = 20, widget = forms.widgets.PasswordInput, label='密码')

