# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-26 16:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ticket', models.IntegerField()),
                ('number_of_question', models.IntegerField()),
                ('picture', models.ImageField(blank=True, upload_to='images_for_quests/')),
                ('question', models.TextField(max_length=2000)),
                ('answer1', models.CharField(max_length=250)),
                ('answer2', models.CharField(max_length=250)),
                ('answer3', models.CharField(blank=True, max_length=250)),
                ('answer4', models.CharField(blank=True, max_length=250)),
                ('answer5', models.CharField(blank=True, max_length=250)),
                ('comment_for_question', models.TextField(max_length=4000)),
            ],
        ),
    ]