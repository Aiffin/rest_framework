# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-16 06:08
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app2', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Snippet',
            new_name='User',
        ),
    ]