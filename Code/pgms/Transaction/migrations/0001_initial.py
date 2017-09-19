# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-18 15:52
from __future__ import unicode_literals

import Transaction.models
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
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Tran_RefNo', models.CharField(max_length=20)),
                ('Tran_File', models.FileField(upload_to='uploaded_files', validators=[Transaction.models.validate_file_extension])),
                ('Date_uploaded', models.DateField(auto_now_add=True)),
                ('StuID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]