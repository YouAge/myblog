# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-14 12:36
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20171214_1428'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='comments_num',
        ),
    ]