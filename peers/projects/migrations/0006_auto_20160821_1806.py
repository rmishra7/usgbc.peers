# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-08-21 18:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0005_auto_20160821_1750'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projectspecificinfo',
            name='all_customer_class',
        ),
        migrations.RemoveField(
            model_name='projectspecificinfo',
            name='all_generator_type',
        ),
        migrations.RemoveField(
            model_name='projectspecificinfo',
            name='meter_aggregation',
        ),
        migrations.RemoveField(
            model_name='projectspecificinfo',
            name='third_party_ownership',
        ),
        migrations.AlterField(
            model_name='projectspecificinfo',
            name='customer_meter_perc',
            field=models.CharField(blank=True, choices=[('RANGE1', 'Less than 5%'), ('RANGE2', 'Between 5% to 50%'), ('RANGE3', '50% or More')], max_length=7, null=True, verbose_name='Customer percentage Installed Advance Meter'),
        ),
    ]