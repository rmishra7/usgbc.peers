# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-08-17 23:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0018_auto_20160817_2351'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectspecificinfo',
            name='bulk_coal',
            field=models.IntegerField(blank=True, default=0, verbose_name='Purchased Bulk Coal Electricity'),
        ),
    ]
