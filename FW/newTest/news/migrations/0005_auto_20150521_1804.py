# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_auto_20141205_2214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='corps',
            field=models.TextField(verbose_name="Corps de l'article"),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='news',
            name='date_debut',
            field=models.DateTimeField(verbose_name='Date de publication désirée'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='news',
            name='date_fin',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Date de fin de publication (laisser vide si aucune expiration voulue)'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='news',
            name='titre',
            field=models.CharField(verbose_name="Titre de l'article", max_length=250),
            preserve_default=True,
        ),
    ]
