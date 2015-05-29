# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('branch', '0055_auto_20150523_0734'),
    ]

    operations = [
        migrations.AddField(
            model_name='offer',
            name='title',
            field=models.CharField(null=True, max_length=120, verbose_name='Titre'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='offerobj',
            name='title',
            field=models.CharField(null=True, max_length=120, verbose_name='Titre'),
            preserve_default=True,
        ),
    ]
