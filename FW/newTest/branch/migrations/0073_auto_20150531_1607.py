# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('branch', '0072_auto_20150530_0759'),
    ]

    operations = [
        migrations.AddField(
            model_name='demand',
            name='estimated_time',
            field=models.IntegerField(blank=True, null=True, verbose_name='Temps estimé (en minutes)'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='demand',
            name='real_time',
            field=models.IntegerField(blank=True, null=True, verbose_name='Temps réel (en minutes)'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='demandobj',
            name='estimated_time',
            field=models.IntegerField(blank=True, null=True, verbose_name='Temps estimé (en minutes)'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='demandobj',
            name='real_time',
            field=models.IntegerField(blank=True, null=True, verbose_name='Temps réel (en minutes)'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='offer',
            name='estimated_time',
            field=models.IntegerField(blank=True, null=True, verbose_name='Temps estimé (en minutes)'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='offer',
            name='real_time',
            field=models.IntegerField(blank=True, null=True, verbose_name='Temps réel (en minutes)'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='offerobj',
            name='estimated_time',
            field=models.IntegerField(blank=True, null=True, verbose_name='Temps estimé (en minutes)'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='offerobj',
            name='real_time',
            field=models.IntegerField(blank=True, null=True, verbose_name='Temps réel (en minutes)'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='successdemand',
            name='time',
            field=models.IntegerField(blank=True, null=True, verbose_name='Temps passé (en minutes)'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='demandpropositionobj',
            name='demand',
            field=models.ForeignKey(blank=True, related_name='propositionsD', null=True, to='branch.Demandobj'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='demandpropositionobj',
            name='offer',
            field=models.ForeignKey(blank=True, related_name='propositionsO', null=True, to='branch.Offerobj'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='successdemand',
            name='demandObj',
            field=models.ForeignKey(blank=True, related_name='success_demandObj', null=True, to='branch.Demandobj'),
            preserve_default=True,
        ),
    ]
