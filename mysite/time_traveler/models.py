# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django import forms


# Create your models here.
class users(models.Model):
    id = models.CharField(max_length=32, primary_key=True)
    uname = models.CharField(max_length=12, db_index=True)
    upassword = models.CharField(max_length=32)
    uuser_email = models.CharField(max_length=32, null=True)
    ufrist_time_password = models.CharField(max_length=32)
    uregistration_time = models.DateTimeField(null=True)
    u_registration_addr = models.CharField(max_length=32, null=True)

    class Meta:
        ordering = ('-uregistration_time',)


class user_form(forms.ModelForm):
    uname = forms.CharField(label=('昵称'), widget=forms.TextInput(attrs={'minlength': '5', 'maxlength': '18'}))
    upassword = forms.CharField(label=("密码"), widget=forms.PasswordInput)
    uuser_email = forms.CharField(label=("邮箱"), widget=forms.EmailInput(attrs={'placeholder': '请输入你的邮箱'}))

    class Meta:
        model = users
        exclude = ('id', 'uregistration_time', 'ufrist_time_password', 'u_registration_addr')
        error_messages = {'uname': {'max_length': ("this writer name is too long")}}
