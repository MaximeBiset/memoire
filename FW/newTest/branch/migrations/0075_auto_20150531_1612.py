# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('branch', '0074_auto_20150531_1611'),
    ]

    operations = [
        migrations.AlterField(
            model_name='demandpropositionobj',
            name='demand',
            field=models.ForeignKey(related_name='propositionsD', null=True, to='branch.Demandobj', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='demandpropositionobj',
            name='offer',
            field=models.ForeignKey(related_name='propositionsO', null=True, to='branch.Offerobj', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='successdemand',
            name='demandObj',
            field=models.ForeignKey(related_name='success_demandObj', null=True, to='branch.Demandobj', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='successdemand',
            name='offerObj',
            field=models.ForeignKey(related_name='success_offerObj', null=True, to='branch.Offerobj', blank=True),
            preserve_default=True,
        ),
    ]
