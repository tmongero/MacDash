# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-01 01:58
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jss', '0016_computer_warranty_expires'),
    ]

    operations = [
        migrations.RenameField(
            model_name='computer',
            old_name='warranty_expires',
            new_name='warranty_expires_utc',
        ),
    ]
