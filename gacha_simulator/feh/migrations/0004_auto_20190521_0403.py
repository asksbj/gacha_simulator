# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2019-05-21 04:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feh', '0003_auto_20190520_2329'),
    ]

    operations = [
        migrations.RenameField(
            model_name='heroes',
            old_name='rarity',
            new_name='rarity_high',
        ),
        migrations.AddField(
            model_name='heroes',
            name='rarity_low',
            field=models.IntegerField(default=None, null=True),
        ),
    ]
