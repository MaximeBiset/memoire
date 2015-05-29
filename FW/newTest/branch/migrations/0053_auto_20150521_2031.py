# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('branch', '0052_auto_20150521_1804'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='demand',
            name='estimated_time',
        ),
        migrations.RemoveField(
            model_name='demand',
            name='real_time',
        ),
        migrations.RemoveField(
            model_name='successdemand',
            name='time',
        ),
    ]
