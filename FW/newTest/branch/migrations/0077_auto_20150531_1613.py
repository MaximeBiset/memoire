# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('branch', '0076_auto_20150531_1612'),
    ]

    operations = [
        migrations.AlterField(
            model_name='successdemand',
            name='demandObj',
            field=models.ForeignKey(blank=True, null=True, to='branch.Demandobj', related_name='success_demandObj'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='successdemand',
            name='offerObj',
            field=models.ForeignKey(blank=True, null=True, to='branch.Offerobj', related_name='success_offerObj'),
            preserve_default=True,
        ),
    ]
