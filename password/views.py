# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views import generic
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render
from .models import Manager,PasswordItems
from user_profile.models import CommonUser
from django.views.generic.list import ListView
from django.utils import timezone

class PasswordListView(generic.ListView):
    model = PasswordItems

    def get_context_data(self, **kwargs):
        context = super(PasswordListView, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context