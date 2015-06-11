# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('branch', '0080_auto_20150607_1406'),
    ]

    operations = [
        migrations.AlterField(
            model_name='demandpropositionobj',
            name='demand',
            field=models.ForeignKey(blank=True, null=True, related_name='propositionsD', to='branch.Demandobj'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='demandpropositionobj',
            name='offer',
            field=models.ForeignKey(blank=True, null=True, related_name='propositionsO', to='branch.Offerobj'),
            preserve_default=True,
        ),
    ]
