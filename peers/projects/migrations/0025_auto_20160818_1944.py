# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-18 19:44
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0024_auto_20160818_0627'),
    ]

    operations = [
        migrations.RenameField(
            model_name='projectspecificinfo',
            old_name='projecr_score',
            new_name='project_score',
        ),
    ]
