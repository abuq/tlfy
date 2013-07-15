# -*- coding:utf-8 -*-

from django.contrib.auth import login, logout
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.http import HttpResponseRedirect
from user_profile.models import UserProfile
from user_profile.forms import *
from lib_tlfy.globals import *

def create_users(request):
    user = User.objects.create(username = 'tlfyadmin', password = '1', is_active = True)
    user.set_password('1')
    user.save()
    UserProfile.objects.create(user = user, name = '管理员')

    return HttpResponseRedirect('/')

def login(request):
    user = request.user
    userp = None
    try:
        userp = UserProfile.objects.get(user = user)
    except:
        pass
    if userp:
        return HttpResponseRedirect('/')

    request.session.set_test_cookie()
    error = list()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            pwd = form.cleaned_data['pwd']

            try:
                user = authenticate(username = username, password = pwd)
                print 'user = ' + str(user)

                if not user:
                    error.append('用户名或密码不正确')
                else:
                    login(request, user)
                    print 'canada'
                    if request.session.test_cookie_worked():
                        request.session.delete_test_cookie()
                    request.session.set_expiry(2592000)
                    if len(error) == 0:
                        return HttpResponseRedirect('/')

            except:
                print 'fail'
                error.append('用户名或密码不正确')
    else:
        form = LoginForm()

    return HttpResponseRedirect('/')

def logout(request):
    logout(request)
    return HttpResponseRedirect('/')

