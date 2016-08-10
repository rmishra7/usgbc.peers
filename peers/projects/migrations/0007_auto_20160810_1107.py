# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-08-10 11:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0006_auto_20160810_0957'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='biomass_elec_capacity',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='Biomass Electricity Generation Capacity'),
        ),
        migrations.AddField(
            model_name='project',
            name='chp_elec_capacity',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='Local CHP natual gas Electricity Generation Capacity'),
        ),
        migrations.AddField(
            model_name='project',
            name='geothermal_elec_capacity',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='Geothermal Electricity Generation Capacity'),
        ),
        migrations.AddField(
            model_name='project',
            name='high_efficiency_gas_elec_capacity',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='Local High Efficiency Electricity generation Capacity'),
        ),
        migrations.AddField(
            model_name='project',
            name='local_other_gas_elec_capacity',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='Local other Gas Electricity Generation Capacity'),
        ),
        migrations.AddField(
            model_name='project',
            name='other_local_elec_capacity',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='Other Renewable Electricity Generation Capacity'),
        ),
        migrations.AddField(
            model_name='project',
            name='tot_local_generation_capacity',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='Total Local Electricity Generation Capacity'),
        ),
        migrations.AddField(
            model_name='project',
            name='turbine_elec_capacity',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='Local Turbine Electricity Generation Capacity'),
        ),
        migrations.AddField(
            model_name='project',
            name='wind_solar_pv_elec_capacity',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='Wind Solar PV Electricity Generation Capacity'),
        ),
    ]
