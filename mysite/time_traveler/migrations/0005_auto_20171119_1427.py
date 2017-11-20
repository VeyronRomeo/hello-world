# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-19 06:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('time_traveler', '0004_auto_20171119_1100'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='ulast_time_login_addr',
            new_name='u_registration_addr',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='ulast_time_password',
            new_name='ufrist_time_password',
        ),
        migrations.RemoveField(
            model_name='user',
            name='ulast_time_login_time',
        ),
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.CharField(max_length=32, primary_key=True, serialize=False),
        ),
    ]