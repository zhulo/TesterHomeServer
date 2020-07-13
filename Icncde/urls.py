# -*- encoding: utf-8 -*-
"""
@File    : urls.py
@Time    : 2020/7/1 15:01
@Author  : tester
@Software: PyCharm
"""
from django.urls import path
from . import views
from Icncde import views

urlpatterns = [
    path('get_access_token', views.post_email_access_token),
]
