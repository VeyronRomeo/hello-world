# -*-coding:utf-8-*-
__author__ = 'VeyronRomeo',
__author_email__ = 'killni.ma@163.com',
__time__ = '2017\11\14 0014 11:18 '
project = "mysite.blog"
"""
description=
"""
from django.conf.urls import *
#from blog.views import archiveView
import blog.views


urlpatterns = [
    url(r'^$', blog.views.archive),
    url(r'^create/', blog.views.create_blogpost),
    #url(r'^$', archiveView.as_view(), name='posts') #通用视图配置

]
