# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('branch', '0068_auto_20150524_1034'),
    ]

    operations = [
        migrations.AddField(
            model_name='demandpropositionobj',
            name='offer',
            field=models.ForeignKey(null=True, to='branch.Offerobj', related_name='propositionsO', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='offerobj',
            name='closed',
            field=models.BooleanField(default=False, verbose_name='Vontaire assigné'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='offerobj',
            name='km',
            field=models.IntegerField(null=True, blank=True, verbose_name='Distance depuis domicile'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='offerobj',
            name='success',
            field=models.NullBooleanField(default=None, verbose_name='Tâche finie avec succès'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='offerobj',
            name='success_fill',
            field=models.BooleanField(default=False, verbose_name='Demande de confirmation envoyée'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='offerobj',
            name='volunteers',
            field=models.ManyToManyField(related_name='volunteersOffObj', blank=True, verbose_name='Propositions', through='branch.DemandPropositionObj', null=True, to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='demandobj',
            name='volunteers',
            field=models.ManyToManyField(related_name='volunteersDemObj', blank=True, verbose_name='Propositions', through='branch.DemandPropositionObj', null=True, to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='demandpropositionobj',
            name='demand',
            field=models.ForeignKey(null=True, to='branch.Demandobj', related_name='propositionsD', blank=True),
            preserve_default=True,
        ),
    ]
