# -*- coding: utf-8 -*-
# Generated by Django 1.11.26 on 2019-12-12 17:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='IrisManagement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sepal_length', models.CharField(blank=True, default=None, max_length=255, null=True)),
                ('sepal_width', models.CharField(blank=True, default=None, max_length=255, null=True)),
                ('petal_length', models.CharField(blank=True, default=None, max_length=255, null=True)),
                ('petal_width', models.CharField(blank=True, default=None, max_length=255, null=True)),
                ('classe', models.CharField(blank=True, default=None, max_length=255, null=True)),
            ],
        ),
    ]
