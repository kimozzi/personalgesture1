# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-11 08:14
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20160210_2344'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='key_expires',
            field=models.DateTimeField(default=datetime.date(2016, 2, 11)),
        ),
    ]
