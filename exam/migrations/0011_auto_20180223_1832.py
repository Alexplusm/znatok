# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-02-23 18:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0010_auto_20180223_1827'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='picture',
            field=models.ImageField(upload_to='images_for_quests/'),
        ),
    ]
