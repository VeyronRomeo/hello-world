# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-19 03:00
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bolgpost',
            options={'ordering': ('-timestamp',)},
        ),
    ]
