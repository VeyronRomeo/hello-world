# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-19 07:38
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('time_traveler', '0005_auto_20171119_1427'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='user',
            new_name='users',
        ),
    ]
