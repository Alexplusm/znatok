# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-01 00:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0002_auto_20171126_1703'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='answer3',
            field=models.CharField(max_length=250, null=True),
        ),
    ]