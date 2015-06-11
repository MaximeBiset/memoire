# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('branch', '0086_auto_20150607_1413'),
    ]

    operations = [
        migrations.AlterField(
            model_name='successofferobj',
            name='offerObj',
            field=models.ForeignKey(to='branch.Offerobj', related_name='success_offerObj', null=True, blank=True),
            preserve_default=True,
        ),
    ]
