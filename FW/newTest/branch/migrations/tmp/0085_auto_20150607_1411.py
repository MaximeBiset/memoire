# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('branch', '0084_auto_20150607_1410'),
    ]

    operations = [
        migrations.AlterField(
            model_name='demandpropositionobj',
            name='offer',
            field=models.ForeignKey(null=True, blank=True, related_name='propositionsO', to='branch.Offerobj'),
            preserve_default=True,
        ),
    ]
