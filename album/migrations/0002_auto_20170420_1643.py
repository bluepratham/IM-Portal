# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-04-20 11:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('album', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='date_create',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]