# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-19 11:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Profile', '0009_auto_20170919_1920'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='br_progress',
            field=models.CharField(choices=[('None', 'None'), ('Proposal Defense', 'Proposal Defense'), ('Work Completion Seminar', 'Work Completion Seminar'), ('Thesis Examination', 'Thesis Examination'), ('Viva Voce', 'Viva Voce'), ('Completed', 'Completed')], default='None', max_length=18, verbose_name='Research Progress'),
        ),
    ]
