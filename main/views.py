#coding=utf-8

from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from user_profile.models import UserProfile
from user_profile.forms import LoginForm
from news.models import *
from notice.models import *
from doc_example.models import *

def main_page(request):
    logged_in = False
    is_admin = False

    user = request.user
    userp = None
    try:
        userp = UserProfile.objects.get(user = user)
    except:
        pass
    if userp:
        logged_in = True
        if userp.is_admin():
            is_admin = True

    form = LoginForm()

    site_start = False
    try:
        userpp = UserProfile.objects.get(id = 1)
    except:
        site_start = True

    news = News.objects.all().filter(type = 0).order_by('-datetime')[0:6]
    intro = News.objects.all().filter(type = 1).order_by('-datetime')[0:6]
    law = News.objects.all().filter(type = 2).order_by('-datetime')[0:6]
    train = News.objects.all().filter(type = 3).order_by('-datetime')[0:6]
    try:
        notice_new = Notice.objects.all().order_by('-datetime')[0]
    except:
        pass
    doc_example = DocExample.objects.all()[0:5]

    return render_to_response('main/main_page.html', RequestContext(request, locals()))
