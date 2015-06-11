# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('branch', '0078_auto_20150601_0620'),
    ]

    operations = [
        migrations.CreateModel(
            name='DemandPropositionOObj',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('comment', models.TextField(blank=True, null=True, verbose_name='Commentaire (facultatif)')),
                ('created', models.DateTimeField(auto_now=True, verbose_name='Date de création')),
                ('accepted', models.BooleanField(verbose_name='Proposition acceptée', default=False)),
                ('km', models.IntegerField(blank=True, null=True, verbose_name='Distance depuis domicile')),
                ('offer', models.ForeignKey(null=True, related_name='propositionsOff', to='branch.OfferObj', blank=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='uservolOObj')),
            ],
            options={
                'ordering': ['-created'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SuccessDemandObj',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('comment', models.TextField(blank=True, null=True, verbose_name='Commentaire')),
                ('created', models.DateTimeField(auto_now=True, verbose_name='Date de création')),
                ('ask_to', models.ForeignKey(null=True, related_name='success_pendingDO', to=settings.AUTH_USER_MODEL, blank=True)),
                ('asked_by', models.ForeignKey(null=True, related_name='approval_pendingDO', to=settings.AUTH_USER_MODEL, blank=True)),
                ('branch', models.ForeignKey(null=True, related_name='success_branch_pendingDO', to='branch.Branch', blank=True)),
                ('demandObj', models.ForeignKey(null=True, related_name='success_demandObj', to='branch.DemandObj', blank=True)),
            ],
            options={
                'ordering': ['-created'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SuccessOfferObj',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('comment', models.TextField(blank=True, null=True, verbose_name='Commentaire')),
                ('created', models.DateTimeField(auto_now=True, verbose_name='Date de création')),
                ('ask_to', models.ForeignKey(null=True, related_name='success_pendingOO', to=settings.AUTH_USER_MODEL, blank=True)),
                ('asked_by', models.ForeignKey(null=True, related_name='approval_pendingOO', to=settings.AUTH_USER_MODEL, blank=True)),
                ('branch', models.ForeignKey(null=True, related_name='success_branch_pendingOO', to='branch.Branch', blank=True)),
                ('offerObj', models.ForeignKey(null=True, related_name='success_offerObj', to='branch.OfferObj', blank=True)),
            ],
            options={
                'ordering': ['-created'],
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='demandpropositionobj',
            name='offer',
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
            field=models.ForeignKey(null=True, related_name='propositionsDem', to='branch.DemandObj', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='offerobj',
            name='volunteers',
            field=models.ManyToManyField(through='branch.DemandPropositionOObj', null=True, related_name='volunteersOffObj', verbose_name='Propositions', to=settings.AUTH_USER_MODEL, blank=True),
            preserve_default=True,
        ),
    ]
