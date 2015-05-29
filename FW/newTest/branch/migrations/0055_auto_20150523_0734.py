# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('branch', '0054_auto_20150522_1617'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='demandobj',
            name='category',
        ),
        migrations.RemoveField(
            model_name='offerobj',
            name='category',
        ),
    ]
