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
import datetime

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
    user = request.user
    userp = None
    try:
        userp = UserProfile.objects.get(user = user)
    except:
        pass
    if not userp:
        return HttpResponseRedirect('/')

    all_doc_example = DocExample.objects.all()
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

