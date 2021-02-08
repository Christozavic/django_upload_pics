# -*-coding:utf-8-*-
# 日期：2021-02-08，时间：13:30

from django.conf.urls import url
from django.urls import path
from .views import upload

app_name = 'pics'

urlpatterns = [
    path('', upload, name='upload'),
]
