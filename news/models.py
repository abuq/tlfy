# -*-coding:utf-8-*-
from django.db import models
from user_profile.models import UserProfile

class News(models.Model):
    title = models.CharField(max_length = 100)
    content = models.TextField()
    datetime = models.DateTimeField()
    picture = models.CharField(max_length = 2000)

    def __unicode__(self):
        return u'%s' % (self.title)
        
    def get_id(self):
        return self.id

    def get_title(self):
        return self.title

    def get_content(self):
        return self.content

    def get_datetime(self):
        return self.datetime

    def get_picture(self):
        pic = self.picture.split('&&')
        print pic
        picture = []
        for p in pic:
            if len(p) != 0:
                picture.append('/media/upload/news/picture/%s' % p)
        
        return picture
