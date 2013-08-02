# -*- coding:utf-8 -*- 
from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, unique = True)
    name = models.CharField(max_length = 100)

    def __unicode__(self):
        return u'%s' % (self.name)

    def get_id(self):
        return self.id

    def is_admin(self):
        if self.user.username == 'superadmin' or self.user.username == 'admin':
            return True
        else:
            return False

    def is_superadmin(self):
        if self.user.username == 'superadmin':
            return True
        else:
            return False

    def get_name(self):
        return self.name
