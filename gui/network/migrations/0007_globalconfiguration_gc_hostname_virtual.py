# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-10-18 16:31
from __future__ import unicode_literals

import django.core.validators
import os
from django.db import migrations, models


SENTINEL = '/data/sentinels/gc_hostname_virtual_out_of_order'


def existing_virtual_hostname(apps, schema_editor):

    if not os.path.exists(SENTINEL):
        return

    with open(SENTINEL, 'r') as f:
        hostname_virtual = f.read().strip().split('\n')[0]

    GlobalConfiguration = apps.get_model('network', 'GlobalConfiguration')
    for o in GlobalConfiguration.objects.all():
        o.gc_hostname_virtual = hostname_virtual
        o.save()


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0006_globalconfiguration_gc_domains'),
    ]

    operations = [
        migrations.AddField(
            model_name='globalconfiguration',
            name='gc_hostname_virtual',
            field=models.CharField(blank=True, max_length=120, null=True, validators=[django.core.validators.RegexValidator(regex='^[a-zA-Z\\.\\-\\_0-9]+$')], verbose_name='Hostname (Virtual)'),
        ),
        migrations.RunPython(existing_virtual_hostname),
    ]
