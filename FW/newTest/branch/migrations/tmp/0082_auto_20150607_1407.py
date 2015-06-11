# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('branch', '0081_auto_20150607_1407'),
    ]

    operations = [
        migrations.AlterField(
            model_name='demandpropositionobj',
            name='demand',
            field=models.ForeignKey(to='branch.Demandobj', related_name='propositionsD', null=True, blank=True),
            preserve_default=True,
        ),
    ]
