# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2017-12-09 18:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0004_auto_20171209_1809'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurantlocation',
            name='category',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
    ]