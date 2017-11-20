# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from django.db import models
from django import forms


# Create your models here.
class BolgPost(models.Model):
    title = models.CharField(max_length=150)
    body = models.TextField()
    timestamp = models.DateTimeField()

    class Meta:
        ordering = ('-timestamp',)


'''
class BlogPostForm(forms.Form):
    title = forms.CharField(max_length=150)
    body = forms.CharField(widget=forms.Textarea(attrs={'row': 3, 'cols': 60}))
    timestamp = forms.DateTimeField()
'''


class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BolgPost
        exclude = ('timestamp',)
