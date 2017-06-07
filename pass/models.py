# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django.db import models

from user_profile.models import CommonUser
# Create your models here.

class PasswordItems(models.Model):
    host_name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    update_time = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.host_name


class Manager(models.Model):
    """
    管理员权限
    """
    user = models.ForeignKey(CommonUser)
    passwords = models.ManyToManyField(PasswordItems)

    def __unicode__(self):
        return self.user.username