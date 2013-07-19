#coding=utf-8
from django.db import models

class DocExample(models.Model):
    title = models.CharField(max_length = 100)
    doc = models.FileField(upload_to = 'doc_example/%Y/%m/%d')

    def _unicode_(self):
        return u'%s' % (self.title)

    def get_title(self):
        return self.title
