# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-11-09 13:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='eventDetails',
            field=models.TextField(default='event details here'),
            preserve_default=False,
        ),
    ]
