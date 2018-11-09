# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-03-20 08:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('engine', '0009_auto_20171218_0641'),
    ]

    operations = [
        migrations.AlterField(
            model_name='version',
            name='name',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterUniqueTogether(
            name='version',
            unique_together=set([('mooclet', 'version_id')]),
        ),
    ]
