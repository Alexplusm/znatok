# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-03-04 21:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_result_is_true'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='birthday',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AddField(
            model_name='profile',
            name='city',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AddField(
            model_name='profile',
            name='user_avatar',
            field=models.ImageField(default='profile_avatar/default.png', upload_to='profile_avatar/'),
        ),
    ]
