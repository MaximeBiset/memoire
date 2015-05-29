# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('branch', '0056_auto_20150523_0800'),
    ]

    operations = [
        migrations.AddField(
            model_name='offerobj',
            name='latitude',
            field=models.CharField(max_length=20, blank=True, verbose_name='Latitude', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='offerobj',
            name='location',
            field=models.CharField(max_length=256, blank=True, verbose_name='Adresse', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='offerobj',
            name='longitude',
            field=models.CharField(max_length=20, blank=True, verbose_name='Longitude', null=True),
            preserve_default=True,
        ),
    ]
