# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-01-02 19:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timetable', '0002_task'),
    ]

    operations = [
        migrations.AlterField(
            model_name='month',
            name='month',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='month',
            name='year',
            field=models.IntegerField(default=1),
        ),
    ]
