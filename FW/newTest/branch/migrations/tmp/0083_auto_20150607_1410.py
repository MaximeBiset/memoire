# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('branch', '0082_auto_20150607_1407'),
    ]

    operations = [
        migrations.AlterField(
            model_name='demandpropositionobj',
            name='demand',
            field=models.ForeignKey(null=True, to='branch.Demandobj', blank=True, related_name='propositionsD'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='demandpropositionobj',
            name='offer',
            field=models.ForeignKey(null=True, to='branch.Offerobj', blank=True, related_name='propositionsO'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='successofferobj',
            name='offerObj',
            field=models.ForeignKey(null=True, to='branch.Offerobj', blank=True, related_name='success_offerObj'),
            preserve_default=True,
        ),
    ]
