# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-08-13 23:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0009_auto_20160813_2245'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectSpecificInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('res_customer', models.IntegerField(blank=True, null=True, verbose_name='No of Residential Customer')),
                ('comm_industrial1', models.IntegerField(blank=True, null=True, verbose_name='No of small commercial and industrial customers')),
                ('comm_industrial2', models.IntegerField(blank=True, null=True, verbose_name='No of large commercial and industrial customers')),
                ('annual_customer_load', models.CharField(blank=True, max_length=20, null=True, verbose_name='Annual Customer Load')),
                ('customer_hr_peak_demand', models.CharField(blank=True, max_length=20, null=True, verbose_name='Customer Annual Hourly Peak Demand')),
                ('peak_demand_unit', models.CharField(default='MW', max_length=10, verbose_name='Peak Demand Unit')),
                ('annual_purchased_elec', models.CharField(blank=True, max_length=20, null=True, verbose_name='Annual Purchased Electricity')),
                ('purchased_hr_peak_demand', models.CharField(blank=True, max_length=10, null=True, verbose_name='Purchased annual hourly peak demand')),
                ('purchased_hr_unit', models.CharField(default='MW', max_length=10, verbose_name='Purchased Peak Demand Unit')),
                ('tnd_losses', models.CharField(blank=True, max_length=10, null=True, verbose_name='T&D Losses')),
                ('tot_local_elec_generation', models.CharField(blank=True, max_length=10, null=True, verbose_name='Total Local Electricity Generation')),
                ('turbine_elec', models.CharField(blank=True, max_length=10, null=True, verbose_name='Local Turbine Electricity Generation')),
                ('chp_elec', models.CharField(blank=True, max_length=10, null=True, verbose_name='Local CHP natual gas Electricity Generation')),
                ('high_efficiency_gas_elec', models.CharField(blank=True, max_length=10, null=True, verbose_name='Local High Efficiency Electricity generation')),
                ('local_other_gas_elec', models.CharField(blank=True, max_length=10, null=True, verbose_name='Local other Gas Electricity Generation')),
                ('wind_solar_pv_elec', models.CharField(blank=True, max_length=10, null=True, verbose_name='Wind Solar PV Electricity Generation')),
                ('biomass_elec', models.CharField(blank=True, max_length=10, null=True, verbose_name='Biomass Electricity Generation')),
                ('geothermal_elec', models.CharField(blank=True, max_length=10, null=True, verbose_name='Geothermal Electricity Generation')),
                ('other_local_elec', models.CharField(blank=True, max_length=10, null=True, verbose_name='Other Renewable Electricity Generation')),
                ('tot_local_generation_capacity', models.CharField(blank=True, max_length=10, null=True, verbose_name='Total Local Electricity Generation Capacity')),
                ('turbine_elec_capacity', models.CharField(blank=True, max_length=10, null=True, verbose_name='Local Turbine Electricity Generation Capacity')),
                ('chp_elec_capacity', models.CharField(blank=True, max_length=10, null=True, verbose_name='Local CHP natual gas Electricity Generation Capacity')),
                ('high_efficiency_gas_elec_capacity', models.CharField(blank=True, max_length=10, null=True, verbose_name='Local High Efficiency Electricity generation Capacity')),
                ('local_other_gas_elec_capacity', models.CharField(blank=True, max_length=10, null=True, verbose_name='Local other Gas Electricity Generation Capacity')),
                ('wind_solar_pv_elec_capacity', models.CharField(blank=True, max_length=10, null=True, verbose_name='Wind Solar PV Electricity Generation Capacity')),
                ('biomass_elec_capacity', models.CharField(blank=True, max_length=10, null=True, verbose_name='Biomass Electricity Generation Capacity')),
                ('geothermal_elec_capacity', models.CharField(blank=True, max_length=10, null=True, verbose_name='Geothermal Electricity Generation Capacity')),
                ('other_local_elec_capacity', models.CharField(blank=True, max_length=10, null=True, verbose_name='Other Renewable Electricity Generation Capacity')),
            ],
            options={
                'verbose_name': 'ProjectSpecificInfo',
                'verbose_name_plural': 'ProjectSpecificInfos',
            },
        ),
        migrations.RemoveField(
            model_name='project',
            name='annual_customer_load',
        ),
        migrations.RemoveField(
            model_name='project',
            name='annual_purchased_elec',
        ),
        migrations.RemoveField(
            model_name='project',
            name='biomass_elec',
        ),
        migrations.RemoveField(
            model_name='project',
            name='biomass_elec_capacity',
        ),
        migrations.RemoveField(
            model_name='project',
            name='chp_elec',
        ),
        migrations.RemoveField(
            model_name='project',
            name='chp_elec_capacity',
        ),
        migrations.RemoveField(
            model_name='project',
            name='comm_industrial1',
        ),
        migrations.RemoveField(
            model_name='project',
            name='comm_industrial2',
        ),
        migrations.RemoveField(
            model_name='project',
            name='currency',
        ),
        migrations.RemoveField(
            model_name='project',
            name='customer_hr_peak_demand',
        ),
        migrations.RemoveField(
            model_name='project',
            name='electricity_unit',
        ),
        migrations.RemoveField(
            model_name='project',
            name='geothermal_elec',
        ),
        migrations.RemoveField(
            model_name='project',
            name='geothermal_elec_capacity',
        ),
        migrations.RemoveField(
            model_name='project',
            name='high_efficiency_gas_elec',
        ),
        migrations.RemoveField(
            model_name='project',
            name='high_efficiency_gas_elec_capacity',
        ),
        migrations.RemoveField(
            model_name='project',
            name='local_other_gas_elec',
        ),
        migrations.RemoveField(
            model_name='project',
            name='local_other_gas_elec_capacity',
        ),
        migrations.RemoveField(
            model_name='project',
            name='other_local_elec',
        ),
        migrations.RemoveField(
            model_name='project',
            name='other_local_elec_capacity',
        ),
        migrations.RemoveField(
            model_name='project',
            name='peak_demand_unit',
        ),
        migrations.RemoveField(
            model_name='project',
            name='purchased_hr_peak_demand',
        ),
        migrations.RemoveField(
            model_name='project',
            name='purchased_hr_unit',
        ),
        migrations.RemoveField(
            model_name='project',
            name='res_customer',
        ),
        migrations.RemoveField(
            model_name='project',
            name='thermal_unit',
        ),
        migrations.RemoveField(
            model_name='project',
            name='tnd_losses',
        ),
        migrations.RemoveField(
            model_name='project',
            name='tot_local_elec_generation',
        ),
        migrations.RemoveField(
            model_name='project',
            name='tot_local_generation_capacity',
        ),
        migrations.RemoveField(
            model_name='project',
            name='turbine_elec',
        ),
        migrations.RemoveField(
            model_name='project',
            name='turbine_elec_capacity',
        ),
        migrations.RemoveField(
            model_name='project',
            name='wind_solar_pv_elec',
        ),
        migrations.RemoveField(
            model_name='project',
            name='wind_solar_pv_elec_capacity',
        ),
        migrations.AddField(
            model_name='projectspecificinfo',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='project_specific', to='projects.Project'),
        ),
    ]