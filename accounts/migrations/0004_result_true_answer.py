# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-02-10 15:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20180210_1502'),
    ]

    operations = [
        migrations.AddField(
            model_name='result',
            name='true_answer',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]