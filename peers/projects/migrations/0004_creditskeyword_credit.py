# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-08-09 19:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_creditskeyword'),
    ]

    operations = [
        migrations.AddField(
            model_name='creditskeyword',
            name='credit',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='credit_keyword', to='projects.CreditsAchieved'),
            preserve_default=False,
        ),
    ]