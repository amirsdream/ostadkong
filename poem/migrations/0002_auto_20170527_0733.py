# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-27 07:33
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('poem', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='poem',
            old_name='name',
            new_name='title',
        ),
    ]
