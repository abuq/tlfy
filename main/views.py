#coding=utf-8

from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from user_profile.models import UserProfile
from user_profile.forms import LoginForm

def main_page(request):
    logged_in = False

    user = request.user
    userp = None
    try:
        userp = UserProfile.objects.get(user = user)
    except:
        pass
    if userp:
        logged_in = True

    form = LoginForm()

    site_start = False
    try:
        userp = UserProfile.objects.get(id = 1)
    except:
        site_start = True
    return render_to_response('main/main_page.html', RequestContext(request, locals()))
