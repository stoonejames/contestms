# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-02 00:39
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contestms', '0002_auto_20160829_1327'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='contest_question',
            unique_together=set([('contest', 'question')]),
        ),
    ]
