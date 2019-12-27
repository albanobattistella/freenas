# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-08-29 04:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storage', '0005_resilver'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuotaExcess',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dataset_name', models.CharField(max_length=256, unique=True)),
                ('level', models.IntegerField()),
                ('used', models.IntegerField()),
                ('available', models.IntegerField()),
                ('percent_used', models.FloatField()),
                ('uid', models.IntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
    ]