# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from .models import BolgPost, BlogPostForm
from django.http import HttpResponseRedirect
from django.template import loader, RequestContext
from datetime import datetime
from django.shortcuts import render_to_response, render
from django.views.generic.base import TemplateView

# Create your views here.
'''
def year_BolgPost(request, title, body, timestamp):
    context = {'title': title, body: 'body', timestamp : 'timestamp'}
    return render(request, '',context)
'''
'''
#通用视图配置
class archiveView(TemplateView):
    template_name = 'archive.html'
    def get_context_data(self, **kwargs):
        posts = super(archiveView,self).get_context_data(**kwargs)
        posts['latest_articles'] = BolgPost.objects.all()[:5]
        return posts
'''


# 数据模型 模式
def archive(request):
    posts = BolgPost.objects.all()
    # t = loader.get_template('archive.html')
    # c = Context({'posts': posts})
    return render(request, 'index.html', {'posts': posts}, RequestContext(request))
    # 'form': BlogPostForm()
    # return render_to_response('archive.html')

'''

#DRY模式
def create_blogpost(request):
    if request.method == 'POST':
        BolgPost(
            title=request.POST.get('title'),
            body=request.POST.get('body'),
            timestamp=datetime.now(),
        ).save()
    return HttpResponseRedirect('/blog/')
'''


def create_blogpost(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.timestamp = datetime.now()
            post.save()
    return HttpResponseRedirect('/blog/')
