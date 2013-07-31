# -*- coding:utf-8 -*- 
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from doc_example.models import *
from doc_example.forms import *
from user_profile.models import UserProfile
from doc_example.models import DocExample
from doc_example.forms import *
from lib_tlfy.globals import *
import datetime
import os

def create_doc_example(request):
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
        form = DocExampleForm(request.POST, request.FILES)
        if form.is_valid():
            title = form.cleaned_data['title']
            docfile = request.FILES['docfile']

            if len(error) == 0:
                doc_example = DocExample.objects.create(title = title, doc =\
                        docfile)
                doc_example.save()
                return HttpResponseRedirect('/')

    else:
        form = DocExampleForm()

    return render_to_response('doc_example/create_doc_example.html',
            RequestContext(request, locals()))

def all_doc_example(request):
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

    all_doc_example = DocExample.objects.filter(type = 0)
    paginator = Paginator(all_doc_example, 10) 

    page = request.GET.get('page')
    try:
        doc_example = paginator.page(page)
    except PageNotAnInteger:
        doc_example = paginator.page(1)
    except EmptyPage:
        doc_example = paginator.page(paginator.num_pages)

    return render_to_response('doc_example/all_doc_example.html',
            RequestContext(request, locals()))

def create_law(request):
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
        form = DocExampleForm(request.POST, request.FILES)
        if form.is_valid():
            title = form.cleaned_data['title']
            docfile = request.FILES['docfile']

            if len(error) == 0:
                doc_example = DocExample.objects.create(title = title, doc =\
                        docfile, type = 1)
                doc_example.save()
                return HttpResponseRedirect('/')

    else:
        form = DocExampleForm()

    return render_to_response('law/create_law.html',
            RequestContext(request, locals()))

def all_law(request):
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

    all_law = DocExample.objects.all().filter(type = 1)
    paginator = Paginator(all_law, 10) 

    page = request.GET.get('page')
    try:
        law = paginator.page(page)
    except PageNotAnInteger:
        law = paginator.page(1)
    except EmptyPage:
        law = paginator.page(paginator.num_pages)

    return render_to_response('law/all_law.html',
            RequestContext(request, locals()))

def delete_doc_example(request, did):
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

    de = DocExample.objects.get(id = int(did))
    print ROOT + '/media/' + de.doc.url
    if os.path.isfile(ROOT + '/media/' + de.doc.url):
        os.remove(ROOT + '/media/' + de.doc.url)
    else:
        pass
    de.delete()
    return HttpResponseRedirect('/doc_example/all/')

