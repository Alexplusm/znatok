# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-07-30 19:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0020_auto_20180704_0845'),
    ]

    operations = [
        migrations.AlterField(
            model_name='result',
            name='true_answer',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='result',
            name='user_answer',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
