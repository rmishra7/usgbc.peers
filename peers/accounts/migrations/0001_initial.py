# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-26 05:53
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Name')),
                ('email', models.EmailField(max_length=70, unique=True, verbose_name='Email')),
                ('username', models.CharField(max_length=32, unique=True, verbose_name='Profilename')),
                ('contact_no', models.CharField(blank=True, max_length=15, null=True, validators=[django.core.validators.RegexValidator('^\\s*(?:\\+?(\\d{1,3}))?[-. (]*(\\d{3})[-. )]*(\\d{3})[-. ]*(\\d{4})(?: *x(\\d+))?\\s*$'), django.core.validators.MinLengthValidator(6), django.core.validators.MaxLengthValidator(15)], verbose_name='Contact Number')),
                ('role', models.CharField(choices=[('1', 'Admin'), ('2', 'User')], default=2, max_length=1, verbose_name='Profile Role')),
                ('email_alerts', models.BooleanField(default=False, verbose_name='Email Alerts')),
                ('sms_alerts', models.BooleanField(default=False, verbose_name='SMS Alerts')),
                ('account_activated', models.BooleanField(default=False, verbose_name='Account Activated')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='Staff Status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='Date Joined')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, verbose_name='Profile Unique ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created On')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Updated On')),
                ('delete', models.BooleanField(default=False, verbose_name='Delete')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'Profile',
                'verbose_name_plural': 'Profiles',
            },
        ),
    ]
