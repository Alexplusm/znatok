# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-07-29 11:04
from __future__ import unicode_literals

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0019_theory'),
    ]

    operations = [
        migrations.CreateModel(
            name='TheoryTheme',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('theme_name', django.contrib.postgres.fields.ArrayField(base_field=models.TextField(), size=None)),
            ],
        ),
    ]