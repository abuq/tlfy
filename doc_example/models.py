#coding=utf-8
from django.db import models
from lib_tlfy.globals import *

class DocExample(models.Model):
    #0:odc_example;1:law
    type = models.IntegerField(default = 0)
    title = models.CharField(max_length = 100)
    doc = models.FileField(upload_to = 'upload/doc_example/')

    def _unicode_(self):
        return u'%s' % (self.title)

    def get_id(self):
        return self.id

    def get_title(self):
        return self.title
