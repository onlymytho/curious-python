# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-20 15:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restapp', '0002_task_task_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='completed',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='task',
            name='task_author',
            field=models.CharField(default='', max_length=200),
        ),
    ]
