#coding=utf-8
from django.db import models

class DocExample(models.Model):
    title = models.CharField(max_length = 100)
    doc_url = models.URLField()

    def _unicode_(self):
        return u'%s' % (self.name)

    def get_title(self):
        return self.title

    def get_doc_url(self):
        return self.doc_url
