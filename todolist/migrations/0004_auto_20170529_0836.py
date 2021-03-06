# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-29 08:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0003_auto_20170527_1240'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Tasklist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='task',
            name='tasklist',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='todolist.Tasklist'),
            preserve_default=False,
        ),
    ]
