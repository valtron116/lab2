# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-01 21:48
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0008_user'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='Register',
        ),
    ]
