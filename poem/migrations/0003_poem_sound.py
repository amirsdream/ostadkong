# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-27 12:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poem', '0002_auto_20170527_0733'),
    ]

    operations = [
        migrations.AddField(
            model_name='poem',
            name='sound',
            field=models.FileField(blank=True, null=True, upload_to='sounds'),
        ),
    ]
