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
    user = User.objects.create(username = 'tlfy', password = '1', is_active = True)
    user.set_password('1')
    user.save()
    userp = UserProfile.objects.create(user = user, name = '管理员')
    print userp.get_name()

    user = User.objects.create(username = 'gaj', password = '1', is_active = True)
    user.set_password('1')
    user.save()
    userp = UserProfile.objects.create(user = user, name = '公安局')
    print userp.get_name()

    user = User.objects.create(username = 'jcy', password = '1', is_active = True)
    user.set_password('1')
    user.save()
    userp = UserProfile.objects.create(user = user, name = '检察院')
    print userp.get_name()

    return HttpResponseRedirect('/')

def log_in(request):
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

                if not user:
                    error.append('用户名或密码不正确')
                else:
                    login(request, user)
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

    return render_to_response('userp/login.html', RequestContext(request, locals()))

def log_out(request):
    logout(request)
    return HttpResponseRedirect('/')

