# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-04-11 08:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0012_auto_20170411_1339'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Product',
            new_name='Products',
        ),
        migrations.AddField(
            model_name='folder',
            name='prob_stat',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
