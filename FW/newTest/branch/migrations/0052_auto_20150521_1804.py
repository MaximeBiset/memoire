# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import multiselectfield.db.fields
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('branch', '0051_merge'),
    ]

    operations = [
        migrations.AlterField(
            model_name='branch',
            name='banned',
            field=models.ManyToManyField(blank=True, related_name='banned_users', to=settings.AUTH_USER_MODEL, null=True, verbose_name='Membres bannis'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='branch',
            name='creator',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, verbose_name='Créateur de la branche'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='branch',
            name='location',
            field=models.CharField(blank=True, null=True, verbose_name='Adresse', max_length=256),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='branch',
            name='members',
            field=models.ManyToManyField(through='branch.BranchMembers', null=True, blank=True, related_name='members', to=settings.AUTH_USER_MODEL, verbose_name='Membres de la branche'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='branch',
            name='name',
            field=models.CharField(verbose_name='Nom de la branche', max_length=255),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='branchmembers',
            name='joined',
            field=models.DateTimeField(verbose_name="date d'arrivé"),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='comment',
            name='comment',
            field=models.TextField(verbose_name='Commentez'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='demand',
            name='branch',
            field=models.ForeignKey(related_name='demand_branch', to='branch.Branch', verbose_name='Branche'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='demand',
            name='category',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('1', 'Visite à la maison'), ('2', 'Tenir compagnie'), ('3', 'Transport par voiture'), ('4', 'Shopping'), ('5', 'Garder des maisons'), ('6', 'Petits boulots manuels'), ('7', 'Jardinage'), ('8', 'Garder des animaux'), ('9', 'Soins personnels'), ('a', 'Administratif'), ('b', 'Autre')], verbose_name="Type d'aide", max_length=21),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='demand',
            name='closed',
            field=models.BooleanField(default=False, verbose_name='Vontaire assigné'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='demand',
            name='donor',
            field=models.ForeignKey(null=True, blank=True, related_name='demand_donor', to=settings.AUTH_USER_MODEL, verbose_name='Donneur'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='demand',
            name='estimated_time',
            field=models.IntegerField(blank=True, null=True, verbose_name='Temps estimé (en minutes)'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='demand',
            name='km',
            field=models.IntegerField(blank=True, null=True, verbose_name='Distance depuis domicile'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='demand',
            name='location',
            field=models.CharField(blank=True, null=True, verbose_name='Adresse', max_length=256),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='demand',
            name='real_time',
            field=models.IntegerField(blank=True, null=True, verbose_name='Temps réel (en minutes)'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='demand',
            name='receive_help_from_who',
            field=models.IntegerField(choices=[(5, 'Tous'), (3, 'Membre vérifié'), (6, 'Mes membres favoris')], default=5, verbose_name='Qui peut voir et répondre à la demande/offre ?'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='demand',
            name='receiver',
            field=models.ForeignKey(null=True, blank=True, related_name='demand_receiver', to=settings.AUTH_USER_MODEL, verbose_name='Receveur'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='demand',
            name='success',
            field=models.NullBooleanField(default=None, verbose_name='Tâche finie avec succès'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='demand',
            name='success_fill',
            field=models.BooleanField(default=False, verbose_name='Demande de confirmation envoyée'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='demand',
            name='time',
            field=multiselectfield.db.fields.MultiSelectField(help_text='Selectionnez les heures qui vous conviennent', choices=[(1, 'Début de matinée (8h-10h)'), (2, 'Fin de matinée (10h-12h)'), (3, 'Midi (12h-13h)'), (4, "Début d'après-midi (13h-16h)"), (5, "Fin d'après-midi (16h-19h)"), (6, 'Repas du soir (19h-20h)'), (7, 'Début de soirée (20h-22h)'), (8, 'Fin de soirée (22h-00h)'), (9, 'Nuit (00h-8h)')], verbose_name='Heures de disponibilité', max_length=17),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='demand',
            name='title',
            field=models.CharField(null=True, verbose_name='Titre', max_length=120),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='demandproposition',
            name='accepted',
            field=models.BooleanField(default=False, verbose_name='Proposition acceptée'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='demandproposition',
            name='comment',
            field=models.TextField(blank=True, null=True, verbose_name='Commentaire (facultatif)'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='demandproposition',
            name='created',
            field=models.DateTimeField(auto_now=True, verbose_name='Date de création'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='demandproposition',
            name='km',
            field=models.IntegerField(blank=True, null=True, verbose_name='Distance depuis domicile'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='demandproposition',
            name='time',
            field=multiselectfield.db.fields.MultiSelectField(help_text='Selectionnez les heures qui vous conviennent', choices=[(1, 'Début de matinée (8h-10h)'), (2, 'Fin de matinée (10h-12h)'), (3, 'Midi (12h-13h)'), (4, "Début d'après-midi (13h-16h)"), (5, "Fin d'après-midi (16h-19h)"), (6, 'Repas du soir (19h-20h)'), (7, 'Début de soirée (20h-22h)'), (8, 'Fin de soirée (22h-00h)'), (9, 'Nuit (00h-8h)')], verbose_name='Heure(s) choisie(s)', max_length=17),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='offer',
            name='branch',
            field=models.ForeignKey(related_name='offer_branch', to='branch.Branch', verbose_name='Branche'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='offer',
            name='category',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('1', 'Visite à la maison'), ('2', 'Tenir compagnie'), ('3', 'Transport par voiture'), ('4', 'Shopping'), ('5', 'Garder des maisons'), ('6', 'Petits boulots manuels'), ('7', 'Jardinage'), ('8', 'Garder des animaux'), ('9', 'Soins personnels'), ('a', 'Administratif'), ('b', 'Autre')], verbose_name="Type d'aide", max_length=21),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='offer',
            name='donor',
            field=models.ForeignKey(null=True, blank=True, related_name='offer_donor', to=settings.AUTH_USER_MODEL, verbose_name='Donneur'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='offer',
            name='receive_help_from_who',
            field=models.IntegerField(choices=[(5, 'Tous'), (3, 'Membre vérifié'), (6, 'Mes membres favoris')], default=5, verbose_name='Qui peut voir et répondre à la demande/offre ?'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='offer',
            name='receiver',
            field=models.ForeignKey(null=True, blank=True, related_name='offer_receiver', to=settings.AUTH_USER_MODEL, verbose_name='Receveur'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='offer',
            name='time',
            field=multiselectfield.db.fields.MultiSelectField(help_text='Selectionnez les heures qui vous conviennent', choices=[(1, 'Début de matinée (8h-10h)'), (2, 'Fin de matinée (10h-12h)'), (3, 'Midi (12h-13h)'), (4, "Début d'après-midi (13h-16h)"), (5, "Fin d'après-midi (16h-19h)"), (6, 'Repas du soir (19h-20h)'), (7, 'Début de soirée (20h-22h)'), (8, 'Fin de soirée (22h-00h)'), (9, 'Nuit (00h-8h)')], verbose_name='Heures de disponibilité', max_length=17),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='successdemand',
            name='comment',
            field=models.TextField(blank=True, null=True, verbose_name='Commentaire'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='successdemand',
            name='created',
            field=models.DateTimeField(auto_now=True, verbose_name='Date de création'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='successdemand',
            name='time',
            field=models.IntegerField(blank=True, null=True, verbose_name='Temps passé (en minutes)'),
            preserve_default=True,
        ),
    ]
