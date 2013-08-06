# -*- coding:utf-8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from message.models import Message
from user_profile.models import UserProfile
from message.forms import SendMessageForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from lib_tlfy.globals import *
import os

def write_page(request):
    user = request.user
    userp = None
    try:
        userp = UserProfile.objects.get(user = user)
    except:
        pass
    if not userp:
        return HttpResponseRedirect('/')

    if request.method == 'POST':
        form = SendMessageForm(request.POST, request.FILES)
        #form = SendMessageForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']
            receivers = form.cleaned_data['receivers']
            try:
                file = request.FILES['file']
                path = '%s%s%s' % (upload_root, 'message/', file.name)
                #print path
                dest = open(path, 'wb+')
                for chunk in file.chunks():
                    dest.write(chunk)
                dest.close()
                #print 'len(receivers):' + str(len(receivers))

                for r in receivers:
                    receiver = UserProfile.objects.get(id = int(r))
                    Message.objects.send_msg(userp, receiver, title, content,
                            len(receivers), 'upload/message/%s' % (file.name))
            except:
                for r in receivers:
                    receiver = UserProfile.objects.get(id = int(r))
                    Message.objects.send_msg(userp, receiver, title, content,
                            0, '')
            return HttpResponseRedirect('/message/inbox/')
    else:
        form = SendMessageForm()
    return render_to_response('message/write_message.html', RequestContext(request,
                locals()))

def inbox(request): 
    logged_in = False;

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

    msg_all = userp.received_msg.all().order_by('-datetime')
    paginator = Paginator(msg_all, 10);
    page = request.GET.get('page')
    try:
        msg = paginator.page(page)
    except PageNotAnInteger:
        msg = paginator.page(1)
    except EmptyPage:
        msg = paginator.page(paginator.num_pages)
    
    return render_to_response('message/inbox.html', RequestContext(request,
                locals()))

def message_page(request, mid):
    user = request.user
    userp = None
    try:
        userp = UserProfile.objects.get(user = user)
    except:
        pass
    if not userp:
        return HttpResponseRedirect('/')

    msg = Message.objects.get(id = int(mid))
    if msg.get_receiver().get_id() != userp.get_id():
        return HttpResponseRedirect('/')

    fujian = False
    if msg.file_url != '':
        fujian = True
        
    return render_to_response('message/message_page.html', RequestContext(request,
                locals()))

def delete_message(request, mid):
    user = request.user
    userp = None
    try:
        userp = UserProfile.objects.get(user = user)
    except:
        pass
    if not userp:
        return HttpResponseRedirect('/')

    msg = Message.objects.get(id = int(mid))
    if msg.get_receiver() != userp:
        return HttpResponseRedirect('/')

    if msg.get_num_file() == 1:
        if os.path.isfile(ROOT + '/media/' + msg.get_file_url()):
            os.remove(ROOT + '/media/' + msg.get_file_url())
        else:
            pass
    else:
        amsg = Message.objects.all().filter(file_url = msg.get_file_url())
        for m in amsg:
            m.minus_num_file(1)
            m.save()

    msg.delete()
    return HttpResponseRedirect('/message/inbox/')
