# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-01 00:48
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jss', '0008_computer_os_version'),
    ]

    operations = [
        migrations.RenameField(
            model_name='computer',
            old_name='warranty_expires_utc',
            new_name='warranty_expires',
        ),
    ]
