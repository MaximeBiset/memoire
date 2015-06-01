# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('branch', '0077_auto_20150531_1613'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='demand',
            name='estimated_time',
        ),
        migrations.RemoveField(
            model_name='demand',
            name='real_time',
        ),
        migrations.RemoveField(
            model_name='demandobj',
            name='estimated_time',
        ),
        migrations.RemoveField(
            model_name='demandobj',
            name='real_time',
        ),
        migrations.RemoveField(
            model_name='offer',
            name='estimated_time',
        ),
        migrations.RemoveField(
            model_name='offer',
            name='real_time',
        ),
        migrations.RemoveField(
            model_name='offerobj',
            name='estimated_time',
        ),
        migrations.RemoveField(
            model_name='offerobj',
            name='real_time',
        ),
        migrations.RemoveField(
            model_name='successdemand',
            name='time',
        ),
        migrations.AlterField(
            model_name='demandpropositionobj',
            name='offer',
            field=models.ForeignKey(to='branch.Offerobj', null=True, related_name='propositionsO', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='successdemand',
            name='demandObj',
            field=models.ForeignKey(to='branch.Demandobj', null=True, related_name='success_demandObj', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='successdemand',
            name='offerObj',
            field=models.ForeignKey(to='branch.Offerobj', null=True, related_name='success_offerObj', blank=True),
            preserve_default=True,
        ),
    ]
