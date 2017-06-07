# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from models import PasswordItems, Manager
# Register your models here.

admin.site.register(PasswordItems)
admin.site.register(Manager)