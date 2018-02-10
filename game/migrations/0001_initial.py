# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-01-31 20:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_of_section', models.IntegerField()),
                ('number_of_pic', models.IntegerField()),
                ('pictureGame', models.ImageField(blank=True, upload_to='images_for_game/')),
            ],
        ),
    ]