# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-11-28 08:44
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wagerapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bets',
            old_name='count',
            new_name='money',
        ),
    ]
