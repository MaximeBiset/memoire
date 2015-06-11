# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('branch', '0079_auto_20150601_0620'),
    ]

    operations = [
        migrations.CreateModel(
            name='SuccessDemandObj',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('comment', models.TextField(verbose_name='Commentaire', blank=True, null=True)),
                ('created', models.DateTimeField(verbose_name='Date de création', auto_now=True)),
                ('ask_to', models.ForeignKey(null=True, blank=True, to=settings.AUTH_USER_MODEL, related_name='success_pendingDO')),
                ('asked_by', models.ForeignKey(null=True, blank=True, to=settings.AUTH_USER_MODEL, related_name='approval_pendingDO')),
                ('branch', models.ForeignKey(null=True, blank=True, to='branch.Branch', related_name='success_branch_pendingDO')),
                ('demandObj', models.ForeignKey(null=True, blank=True, to='branch.Demandobj', related_name='success_demandObj')),
            ],
            options={
                'ordering': ['-created'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SuccessOfferObj',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('comment', models.TextField(verbose_name='Commentaire', blank=True, null=True)),
                ('created', models.DateTimeField(verbose_name='Date de création', auto_now=True)),
                ('ask_to', models.ForeignKey(null=True, blank=True, to=settings.AUTH_USER_MODEL, related_name='success_pendingOO')),
                ('asked_by', models.ForeignKey(null=True, blank=True, to=settings.AUTH_USER_MODEL, related_name='approval_pendingOO')),
                ('branch', models.ForeignKey(null=True, blank=True, to='branch.Branch', related_name='success_branch_pendingOO')),
                ('offerObj', models.ForeignKey(null=True, blank=True, to='branch.Offerobj', related_name='success_offerObj')),
            ],
            options={
                'ordering': ['-created'],
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='successdemand',
            name='demandObj',
        ),
        migrations.RemoveField(
            model_name='successdemand',
            name='offerObj',
        ),
        migrations.AlterField(
            model_name='demandpropositionobj',
            name='demand',
            field=models.ForeignKey(null=True, blank=True, to='branch.Demandobj', related_name='propositionsD'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='demandpropositionobj',
            name='offer',
            field=models.ForeignKey(null=True, blank=True, to='branch.Offerobj', related_name='propositionsO'),
            preserve_default=True,
        ),
    ]
