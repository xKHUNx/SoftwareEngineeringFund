# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-01 08:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Profile', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='stud_type',
            field=models.IntegerField(blank=True, choices=[(0, 'By Research'), (1, 'By Coursework')], null=True, verbose_name='Student Type'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='user_photo',
            field=models.FileField(blank=True, default='', null=True, upload_to='', verbose_name='Profile Picture'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='user_status',
            field=models.IntegerField(blank=True, choices=[(0, 'Active'), (1, 'Terminated'), (2, 'Graduated')], null=True, verbose_name='Academic Status'),
        ),
    ]