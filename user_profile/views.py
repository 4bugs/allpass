# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,get_object_or_404
from .models import CommonUser

# Create your views here.
def users(request, user_id):
    userprofile = get_object_or_404(CommonUser, pk=user_id)
    return render(request, 'user_profile/users.html', {'userprofile': userprofile})