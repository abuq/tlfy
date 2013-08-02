# -*- coding:utf-8 -*-
from django.contrib import admin
from user_profile.models import *

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'name')
    search_field = ('user', 'name')

admin.site.register(UserProfile, UserProfileAdmin)
