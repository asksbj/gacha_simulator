# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2019-05-25 18:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feh', '0002_heroes_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pools',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=None, max_length=128, null=True)),
                ('start_date', models.DateField(default=None, null=True)),
                ('end_date', models.DateField(default=None, null=True)),
                ('start5_focus', models.DecimalField(decimal_places=6, default=None, max_digits=18, null=True)),
                ('start5', models.DecimalField(decimal_places=6, default=None, max_digits=18, null=True)),
                ('start4', models.DecimalField(decimal_places=6, default=None, max_digits=18, null=True)),
                ('start3', models.DecimalField(decimal_places=6, default=None, max_digits=18, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='pools',
            name='featured_units',
            field=models.ManyToManyField(to='feh.Heroes'),
        ),
    ]
