# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('branch', '0073_auto_20150531_1607'),
    ]

    operations = [
        migrations.AlterField(
            model_name='demandpropositionobj',
            name='demand',
            field=models.ForeignKey(related_name='propositionsD', null=True, blank=True, to='branch.Demandobj'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='demandpropositionobj',
            name='offer',
            field=models.ForeignKey(related_name='propositionsO', null=True, blank=True, to='branch.Offerobj'),
            preserve_default=True,
        ),
    ]
