# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from datetime import datetime
from django.test.client import Client
from blog.models import BolgPost


# Create your tests here.

class BlogPostTest(TestCase):
    def test_obj_create(self):
        BolgPost.objects.create(title='raw title',
                                body='raw body', timestamp=datetime.now())
        self.assertAlmostEqual(1, BolgPost.objects.count())
        self.assertAlmostEqual('raw title', BolgPost.objects.get(id=1).title)

    def test_home(self):
        response = self.client.get('/blog/')
        self.failUnlessEqual(response.status_code, 200)

    def test_empty_create(self):
        response = self.client.get('/blog/create/')
        self.assertIn(response.status_code, (301, 302))

    def test_post_create(self):
        response = self.client.post('/blog/create/', {
            'title': 'post title',
            'body': 'post body',
        })
        self.assertIn(response.status_code, (301, 302))
        self.assertEqual(1, BolgPost.objects.count())
        self.assertEqual('post title', BolgPost.objects.get(id=1).title)

    def test_slash(self):
        response = self.client.get('/')
        self.assertIn(response.status_code, (301, 302))
