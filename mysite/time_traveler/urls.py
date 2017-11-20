# -*-coding:utf-8-*-
__author__ = 'VeyronRomeo',
__author_email__ = 'killni.ma@163.com',
__time__ = '2017\11\19 0019 11:02 '
project = 'time_traveler'
"""
description=
"""

from django.conf.urls import *

try:
    from time_traveler import views as ui, models
except:
    print 'time_traveler import err'

urlpatterns = [
    url(r'^$', ui.time_index),
    url(r'^create/', ui.user_create),
    url(r'^logined/', ui.user_login),
    url(r'^login/',ui.login),
    url(r'^valide_name/',ui.valide_name),
]
