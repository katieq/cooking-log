# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-04 00:50
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cooklog', '0004_auto_20161204_0030'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe_method',
            name='recipe_id',
        ),
        migrations.DeleteModel(
            name='Recipe_Method',
        ),
    ]
