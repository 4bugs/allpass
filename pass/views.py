# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views import generic
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render
from .models import Manager,PasswordItems

class PasswordView(generic.DetailView):
    model = PasswordItems
    template_name = 'pass/password.html'
