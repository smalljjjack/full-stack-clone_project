# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-01-18 03:14
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='create_data',
        ),
        migrations.RemoveField(
            model_name='post',
            name='create_data',
        ),
        migrations.AddField(
            model_name='comment',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 1, 18, 3, 14, 29, 436768, tzinfo=utc)),
        ),
        migrations.AddField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 1, 18, 3, 14, 29, 435766, tzinfo=utc)),
        ),
    ]
