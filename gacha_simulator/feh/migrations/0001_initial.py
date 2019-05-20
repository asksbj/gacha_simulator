# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2019-05-20 01:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Heros',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=None, max_length=64, null=True)),
                ('gender', models.CharField(choices=[('male', 'male'), ('female', 'female')], default=None, max_length=6, null=True)),
                ('rarity', models.IntegerField(default=None, null=True)),
                ('weapon_type', models.CharField(default=None, max_length=32, null=True)),
            ],
        ),
    ]