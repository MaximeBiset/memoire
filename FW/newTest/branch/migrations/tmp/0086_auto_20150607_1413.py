# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('branch', '0085_auto_20150607_1411'),
    ]

    operations = [
        migrations.AlterField(
            model_name='demandpropositionobj',
            name='demand',
            field=models.ForeignKey(blank=True, related_name='propositionsDem', to='branch.Demandobj', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='demandpropositionobj',
            name='offer',
            field=models.ForeignKey(blank=True, related_name='propositionsOff', to='branch.Offerobj', null=True),
            preserve_default=True,
        ),
    ]
