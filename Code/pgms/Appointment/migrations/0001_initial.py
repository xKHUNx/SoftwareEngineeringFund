# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-19 02:41
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('status', models.CharField(choices=[('Approve', 'Approve'), ('Reject', 'Reject'), ('Pending', 'Pending')], default='Pending', max_length=7)),
                ('reason', models.CharField(max_length=200)),
                ('lecID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='lecID', to=settings.AUTH_USER_MODEL)),
                ('stuID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='stuID', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
