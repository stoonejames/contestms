# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-03 12:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contestms', '0004_example'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='hint',
            field=models.TextField(null=True),
        ),
    ]
