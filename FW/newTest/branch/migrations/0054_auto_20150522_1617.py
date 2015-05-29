# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import multiselectfield.db.fields
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('branch', '0053_auto_20150521_2031'),
    ]

    operations = [
        migrations.CreateModel(
            name='DemandObj',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('description', models.TextField(verbose_name='Description', null=True, blank=True)),
                ('receive_help_from_who', models.IntegerField(verbose_name='Qui peut voir et répondre à la demande/offre ?', choices=[(5, 'Tous'), (3, 'Membre vérifié'), (6, 'Mes membres favoris')], default=5)),
                ('date', models.DateTimeField(verbose_name='Date')),
                ('category', multiselectfield.db.fields.MultiSelectField(verbose_name="Type d'aide", choices=[('1', 'Visite à la maison'), ('2', 'Tenir compagnie'), ('3', 'Transport par voiture'), ('4', 'Shopping'), ('5', 'Garder des maisons'), ('6', 'Petits boulots manuels'), ('7', 'Jardinage'), ('8', 'Garder des animaux'), ('9', 'Soins personnels'), ('a', 'Administratif'), ('b', 'Autre')], max_length=21)),
                ('title', models.CharField(verbose_name='Titre', null=True, max_length=120)),
                ('location', models.CharField(verbose_name='Adresse', null=True, max_length=256, blank=True)),
                ('latitude', models.CharField(verbose_name='Latitude', null=True, max_length=20, blank=True)),
                ('longitude', models.CharField(verbose_name='Longitude', null=True, max_length=20, blank=True)),
                ('closed', models.BooleanField(verbose_name='Vontaire assigné', default=False)),
                ('success_fill', models.BooleanField(verbose_name='Demande de confirmation envoyée', default=False)),
                ('km', models.IntegerField(verbose_name='Distance depuis domicile', null=True, blank=True)),
                ('success', models.NullBooleanField(verbose_name='Tâche finie avec succès', default=None)),
                ('branch', models.ForeignKey(related_name='demandobj_branch', to='branch.Branch', verbose_name='Branche')),
                ('donor', models.ForeignKey(null=True, related_name='demandobj_donor', blank=True, verbose_name='Donneur', to=settings.AUTH_USER_MODEL)),
                ('receiver', models.ForeignKey(null=True, related_name='demandobj_receiver', blank=True, verbose_name='Receveur', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['date'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DemandPropositionObj',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('comment', models.TextField(verbose_name='Commentaire (facultatif)', null=True, blank=True)),
                ('created', models.DateTimeField(verbose_name='Date de création', auto_now=True)),
                ('accepted', models.BooleanField(verbose_name='Proposition acceptée', default=False)),
                ('km', models.IntegerField(verbose_name='Distance depuis domicile', null=True, blank=True)),
                ('demand', models.ForeignKey(related_name='propositions', to='branch.DemandObj')),
                ('user', models.ForeignKey(related_name='uservolObj', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='OfferObj',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('description', models.TextField(verbose_name='Description', null=True, blank=True)),
                ('receive_help_from_who', models.IntegerField(verbose_name='Qui peut voir et répondre à la demande/offre ?', choices=[(5, 'Tous'), (3, 'Membre vérifié'), (6, 'Mes membres favoris')], default=5)),
                ('date', models.DateTimeField(verbose_name='Date')),
                ('category', multiselectfield.db.fields.MultiSelectField(verbose_name="Type d'aide", choices=[('1', 'Visite à la maison'), ('2', 'Tenir compagnie'), ('3', 'Transport par voiture'), ('4', 'Shopping'), ('5', 'Garder des maisons'), ('6', 'Petits boulots manuels'), ('7', 'Jardinage'), ('8', 'Garder des animaux'), ('9', 'Soins personnels'), ('a', 'Administratif'), ('b', 'Autre')], max_length=21)),
                ('branch', models.ForeignKey(related_name='offerobj_branch', to='branch.Branch', verbose_name='Branche')),
                ('donor', models.ForeignKey(null=True, related_name='offerobj_donor', blank=True, verbose_name='Donneur', to=settings.AUTH_USER_MODEL)),
                ('receiver', models.ForeignKey(null=True, related_name='offerobj_receiver', blank=True, verbose_name='Receveur', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['date'],
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='demandobj',
            name='volunteers',
            field=models.ManyToManyField(null=True, related_name='volunteersObj', blank=True, verbose_name='Propositions', to=settings.AUTH_USER_MODEL, through='branch.DemandPropositionObj'),
            preserve_default=True,
        ),
    ]
