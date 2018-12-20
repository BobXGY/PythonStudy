#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# @author Bob
# @create time 2018/12/20 14:38
# @file view.py
# @software PyCharm
from django.http import HttpResponse


def hello(request):
    return HttpResponse("hello django")
