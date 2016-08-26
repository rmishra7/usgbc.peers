# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-08-25 16:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0008_auto_20160825_1520'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectspecificinfo',
            name='lre_score',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='LRE Strategy Score'),
        ),
        migrations.AlterField(
            model_name='projectspecificinfo',
            name='net_metering_score',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Net Metering Score'),
        ),
        migrations.AlterField(
            model_name='projectspecificinfo',
            name='oe_credit_score',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='OE Credit Score'),
        ),
        migrations.AlterField(
            model_name='projectspecificinfo',
            name='sei_score',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Project Score'),
        ),
    ]