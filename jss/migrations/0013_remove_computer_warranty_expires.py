# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-01 01:45
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jss', '0012_auto_20160601_0142'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='computer',
            name='warranty_expires',
        ),
    ]
