# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-25 22:45
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20170725_1942'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comentario',
            name='data_publicacao',
            field=models.DateTimeField(default=datetime.datetime(2017, 7, 25, 22, 45, 43, 701707, tzinfo=utc)),
        ),
    ]
