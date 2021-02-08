# -*-coding:utf-8-*-
# 日期：2021-02-08，时间：14:02

from django import forms


class PicsForm(forms.Form):
    pic_file = forms.ImageField(label='pic')
