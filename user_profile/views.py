# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,get_object_or_404
from .models import CommonUser
from django.contrib.auth.decorators import login_required

@login_required
def users(request, user_id):
    userprofile = get_object_or_404(CommonUser, pk=user_id)
    return render(request, '../templates/user_profile/users.html', {'userprofile': userprofile})

