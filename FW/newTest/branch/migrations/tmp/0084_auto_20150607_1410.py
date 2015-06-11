# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('branch', '0083_auto_20150607_1410'),
    ]

    operations = [
        migrations.AlterField(
            model_name='demandpropositionobj',
            name='demand',
            field=models.ForeignKey(related_name='propositionsD', to='branch.Demandobj', blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='demandpropositionobj',
            name='offer',
            field=models.ForeignKey(related_name='propositionsO', to='branch.Offerobj', blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='successofferobj',
            name='offerObj',
            field=models.ForeignKey(related_name='success_offerObj', to='branch.Offerobj', blank=True, null=True),
            preserve_default=True,
        ),
    ]
