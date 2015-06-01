# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('branch', '0078_auto_20150601_0620'),
    ]

    operations = [
        migrations.AlterField(
            model_name='successdemand',
            name='demandObj',
            field=models.ForeignKey(to='branch.Demandobj', null=True, related_name='success_demandObj', blank=True),
            preserve_default=True,
        ),
    ]
