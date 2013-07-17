# -*- coding:utf-8 -*-
from django.db import models
from user_profile.models import UserProfile
import datetime

class MessageManager(models.Manager):
    def send_msg(self, sender, receiver, title, content):
        msg = self.create(
                sender = sender,
                receiver = receiver,
                title = title,
                content = content,
                status = 0,
                datetime = datetime.datetime.now(),
                )
        msg.save()
        return msg

class Message(models.Model):
    sender = models.ForeignKey(UserProfile, related_name = 'send_msg')
    receiver = models.ForeignKey(UserProfile, related_name = 'received_msg')
    title = models.CharField(max_length = 100)
    content = models.CharField(max_length = 1000)
    status = models.IntegerField(default = 0)#0:intact,1:read.
    datetime = models.DateTimeField()

    objects = MessageManager()

    def get_id(self):
        return self.id

    def get_sender(self):
        return self.sender

    def get_receiver(self):
        return self.receiver

    def get_title(self):
        return self.title

    def get_content(self):
        return self.content

    def get_status(self):
        return self.status

    def already_read(self):
        self.status = 1
        self.save()
        return self.status

    def get_datetime(self):
        return self.datetime

    def __unicode__(self):
        return u'%s' % (self.title)
