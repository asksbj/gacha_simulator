# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2019-05-21 22:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feh', '0004_auto_20190521_0403'),
    ]

    operations = [
        migrations.RenameField(
            model_name='heroes',
            old_name='type',
            new_name='hero_type',
        ),
        migrations.AddField(
            model_name='heroes',
            name='art_by',
            field=models.CharField(default=None, max_length=32, null=True),
        ),
    ]
