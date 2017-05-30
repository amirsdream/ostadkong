# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-27 07:19
from __future__ import unicode_literals

from django.db import migrations, models
import stdimage.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Poem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('text', models.TextField(null=True)),
                ('image', stdimage.models.StdImageField(blank=True, null=True, upload_to='blogimage')),
            ],
        ),
    ]