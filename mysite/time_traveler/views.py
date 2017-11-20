# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.template import RequestContext
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from .models import user_form,users
from datetime import datetime
import hashlib, time


# Create your views here.
def time_index(request):
    return render(request, 'registration.html', {'form': user_form()})

'''
用户
注册处理。
'''
def user_create(request):
    if request.method == 'POST':
        form = user_form(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.id = ceate_Id()

            post.upassword = password_create(post.upassword)
            post.ufrist_time_password = post.upassword
            post.uregistration_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            # post.ulast_time_login_time = datetime.now()
            if request.META.has_key('HTTP_X_FORWARDED_FOR'):
                ip = request.META['HTTP_X_FORWARDED_FOR']
            else:
                ip = request.META['REMOTE_ADDR']
            post.u_registration_addr = ip
            if uname_unque(post.uname):
                pass
            else:
                post.save()
    return HttpResponseRedirect('/time_trl/')



#对name值限制必须以字符开头,函数固定格式valide_field
def valide_name(request):
    if request.method == "GET" and request.GET:
        uname = request.GET['uname']
        if users.objects.filter(uname=uname):
#        if name == id_name:
            uname = "we have a %s" % uname
        else:
            uname = uname
    else:
        uname = "No name"
    result = {"data":uname}
    return JsonResponse(result)


def user_login(request):
    if request.method == 'POST':
        uname = request.POST.get('uname')
        psw = request.POST.get('upasswrod')
        login_verify(uname,psw)
        print uname + psw
    return HttpResponseRedirect('/time_trl/',RequestContext(request))


def login(request):
    return render(request, 'login.html')


def ceate_Id():
    id = hashlib.md5(str(time.clock()).encode('utf-8')).hexdigest()
    return id


def password_create(psw):
    m = hashlib.md5()
    m.update(psw)
    return m.hexdigest()

def login_verify(name,psw):
    user = users.objects.get(uname=name)
    if user is not None:
        password = user.upassword
        print type(password)
        print password

    return 'success'

def uname_unque(name):
    if users.objects.get(uname = name):
        return False
    else:
        return True
