# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('branch', '0070_auto_20150528_1324'),
    ]

    operations = [
        migrations.AlterField(
            model_name='demandpropositionobj',
            name='demand',
            field=models.ForeignKey(to='branch.Demandobj', related_name='propositionsD', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='demandpropositionobj',
            name='offer',
            field=models.ForeignKey(to='branch.Offerobj', related_name='propositionsO', null=True, blank=True),
            preserve_default=True,
        ),
    ]
