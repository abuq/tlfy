# -*- coding:utf-8 -*- 
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from news.models import *
from news.forms import *
from lib_tlfy.globals import *
import datetime

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

            if len(error) == 0:
                news = News.objects.create(title = title, content = content,
                        datetime = datetime.datetime.now())
                news.save()
                return HttpResponseRedirect('/')

    else:
        form = NewsForm()

    return render_to_response('news/create_news.html',
            RequestContext(request, locals()))

def news_page(request, nid):
    news = News.objects.get(id = int(nid))

    if request.method == 'POST':
        form = PictureForm(request.POST)
        if form.is_valid():
            if 'file' in request.FILES:
                file = request.FILES['file']
                path = '%s%s%s%s' % (upload_root, 'news/picture/', news.get_id(),
                        file.name)
                print 'path=' + path
                dest = open(path, 'wb+')
                
                for chunk in file.chunks():
                    dest.write(chunk)
                dest.close()
                print news.picture
                print news.get_id()
                print file.name
                news.picture = '%s%d%s&&' % (news.picture, news.get_id(), file.name)
                news.save()
    else:
        form = PictureForm()

    picture = news.get_picture()
    
    print 'picture=' + str(picture)

    return render_to_response('news/news_page.html',
            RequestContext(request, locals()))

def all_news(request):
    anews = News.objects.all().order_by('-datetime')
    paginator = Paginator(anews, 12) # Show 25 contacts per page

    page = request.GET.get('page')
    try:
        anews_part = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        anews_part = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        anews_part = paginator.page(paginator.num_pages)

    return render_to_response('news/all_news.html',
            RequestContext(request, locals()))

