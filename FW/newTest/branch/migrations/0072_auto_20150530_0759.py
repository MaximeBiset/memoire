# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('branch', '0071_auto_20150528_1403'),
    ]

    operations = [
        migrations.AddField(
            model_name='successdemand',
            name='demandObj',
            field=models.ForeignKey(blank=True, related_name='success_demandObj', null=True, to='branch.Demandobj'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='successdemand',
            name='offerObj',
            field=models.ForeignKey(blank=True, related_name='success_offerObj', null=True, to='branch.Offerobj'),
            preserve_default=True,
        ),
    ]
