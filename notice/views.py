# -*- coding:utf-8 -*- 
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from notice.models import *
from notice.forms import *
from user_profile.models import UserProfile
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

import datetime

def create_notice(request):
    user = request.user
    userp = None
    try:
        userp = UserProfile.objects.get(user = user)
    except:
        pass
    if not userp:
        return HttpResponseRedirect('/')

    if not userp.is_admin():
        return HttpResponseRedirect('/')

    if request.method == 'POST':
        form = NoticeForm(request.POST)
        if form.is_valid():
            content = form.cleaned_data['content']

        ntc = Notice.objects.create(content = content,
                datetime = datetime.datetime.now())
        ntc.save()
        return HttpResponseRedirect('/')

    else:
        form = NoticeForm()

    return render_to_response('notice/create_notice.html', RequestContext(request, locals()))

def all_notice(request):
    logged_in = False
    is_superadmin = False

    user = request.user
    userp = None
    try:
        userp = UserProfile.objects.get(user = user)
    except:
        pass
    if not userp:
        return HttpResponseRedirect('/')
    else:
        logged_in = True
        if userp.is_superadmin():
            is_superadmin = True

    notice_all = Notice.objects.all().order_by('-datetime')
    paginator = Paginator(notice_all, 10)

    page = request.GET.get('page')
    try:
        notice = paginator.page(page)
    except PageNotAnInteger:
        notice = paginator.page(1)
    except EmptyPage:
        notice = paginator.page(paginator.num_pages)

    return render_to_response('notice/all_notice.html',
            RequestContext(request, locals()))

def delete_notice(request, nid):
    user = request.user
    userp = None
    try:
        userp = UserProfile.objects.get(user = user)
    except:
        pass
    if not userp:
        return HttpResponseRedirect('/')
    elif not userp.is_superadmin():
        return HttpResponseRedirect('/')

    notice = Notice.objects.get(id = int(nid))
    notice.delete()

    return HttpResponseRedirect('/notice/all/')
