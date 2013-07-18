#coding=utf-8
from django.db import models

class Notice(models.Model):
    content = models.CharField(max_length = 1000)
    datetime = models.DateTimeField()

    def __unicode__(self):
        return u'%s' % (self.content)

    def get_content(self):
        return self.content

    def get_datetime(self):
        return self.datetime
