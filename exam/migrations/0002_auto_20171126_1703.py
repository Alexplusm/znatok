# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-26 17:03
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='ticket',
            new_name='number_of_ticket',
        ),
    ]
