# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2017-12-09 19:01
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0008_auto_20171209_1900'),
    ]

    operations = [
        migrations.RenameField(
            model_name='restaurantlocation',
            old_name='update',
            new_name='updated',
        ),
    ]