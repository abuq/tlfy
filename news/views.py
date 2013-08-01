# -*- coding:utf-8 -*- 
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from news.models import *
from news.forms import *
from lib_tlfy.globals import *
import datetime
import os

def create_news(request):
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

    error = list()
    if request.method == 'POST':
        form = NewsForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']

            content = content.replace(' ', '&nbsp;')
            content = content.replace('\r\n', '<br \>')
            content = content.replace('\n', '<br \>')

            if len(error) == 0:
                news = News.objects.create(title = title, content = content,
                        datetime = datetime.datetime.now())
                news.save()
                return HttpResponseRedirect('/')

    else:
        form = NewsForm()

    return render_to_response('news/create_news.html',
            RequestContext(request, locals()))

def create_intro(request):
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

    error = list()
    if request.method == 'POST':
        form = NewsForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']

            if len(error) == 0:
                news = News.objects.create(title = title, content = content,
                        datetime = datetime.datetime.now(), type = 1)
                news.save()
                return HttpResponseRedirect('/')

    else:
        form = NewsForm()

    return render_to_response('intro/create_intro.html',
            RequestContext(request, locals()))

def create_train(request):
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

    error = list()
    if request.method == 'POST':
        form = NewsForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']

            if len(error) == 0:
                news = News.objects.create(title = title, content = content,
                        datetime = datetime.datetime.now(), type = 3)
                news.save()
                return HttpResponseRedirect('/')

    else:
        form = NewsForm()

    return render_to_response('train/create_train.html',
            RequestContext(request, locals()))

def all_news(request):
    logged_in = False
    user = request.user
    userp = None
    try:
        userp = UserProfile.objects.get(user = user)
    except:
        pass
    if not userp:
        pass
    else:
        logged_in = True

    anews = News.objects.all().filter(type = 0).order_by('-datetime')
    paginator = Paginator(anews, 12) 

    page = request.GET.get('page')
    try:
        anews_part = paginator.page(page)
    except PageNotAnInteger:
        anews_part = paginator.page(1)
    except EmptyPage:
        anews_part = paginator.page(paginator.num_pages)

    return render_to_response('news/all_news.html',
            RequestContext(request, locals()))

def all_intro(request):
    logged_in = False
    user = request.user
    userp = None
    try:
        userp = UserProfile.objects.get(user = user)
    except:
        pass
    if not userp:
        pass
    else:
        logged_in = True

    aintro = News.objects.all().filter(type = 1).order_by('-datetime')
    paginator = Paginator(aintro, 12) 

    page = request.GET.get('page')
    try:
        intro = paginator.page(page)
    except PageNotAnInteger:
        intro = paginator.page(1)
    except EmptyPage:
        intro = paginator.page(paginator.num_pages)

    return render_to_response('intro/all_intro.html',
            RequestContext(request, locals()))

def all_train(request):
    logged_in = False
    user = request.user
    userp = None
    try:
        userp = UserProfile.objects.get(user = user)
    except:
        pass
    if not userp:
        pass
    else:
        logged_in = True

    atrain = News.objects.all().filter(type = 3).order_by('-datetime')
    paginator = Paginator(atrain, 12) 

    page = request.GET.get('page')
    try:
        train = paginator.page(page)
    except PageNotAnInteger:
        train = paginator.page(1)
    except EmptyPage:
        train = paginator.page(paginator.num_pages)

    return render_to_response('train/all_train.html',
            RequestContext(request, locals()))

def news_page(request, nid):
    logged_in = False
    is_admin = False
    is_superadmin = False

    user = request.user
    userp = None
    try:
        userp = UserProfile.objects.get(user = user)
    except:
        pass
    if not userp:
        pass
    else:
        logged_in = True
        if userp.is_admin():
            is_admin = True
        if userp.is_superadmin():
            is_superadmin = True

    news = News.objects.get(id = int(nid))

    if request.method == 'POST':
        form = PictureForm(request.POST)
        if form.is_valid():
            if 'file' in request.FILES:
                file = request.FILES['file']
                path = '%s%s%s%s%s' % (upload_root, 'news/picture/', news.get_id(),
                        '$_$', file.name)
                dest = open(path, 'wb+')
                
                for chunk in file.chunks():
                    dest.write(chunk)
                dest.close()
                news.picture = '%s%d%s%s&_&' % (news.picture, news.get_id(),
                        '$_$', file.name)
                news.save()
    else:
        form = PictureForm()

    picture = news.get_picture()
    return render_to_response('news/news_page.html',
            RequestContext(request, locals()))

def delete_news(request, nid):
    user = request.user
    userp = None
    try:
        userp = UserProfile.objects.get(user = user)
    except:
        pass
    if not userp:
        return HttpResponseRedirect('/')
    else:
        if not userp.is_superadmin():
            return HttpResponseRedirect('/')

    news = News.objects.get(id = int(nid))
    picture = news.get_picture()
    for p in picture:
        if os.path.isfile(ROOT + p):
            os.remove(ROOT + p)
        else:   
            pass

    news.delete()
    return HttpResponseRedirect('/news/all/')

    
