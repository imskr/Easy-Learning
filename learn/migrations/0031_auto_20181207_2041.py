# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-12-07 15:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learn', '0030_auto_20171209_1519'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vote',
            name='value',
            field=models.IntegerField(choices=[(1, 'Upvote'), (0, 'Undo'), (-1, 'DownVote')], default=1),
        ),
    ]
