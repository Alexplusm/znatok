# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-02-23 18:40
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0012_auto_20180223_1835'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='category',
        ),
    ]