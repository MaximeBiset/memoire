# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0043_remove_user_credit'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='credit',
            field=models.IntegerField(default=0, verbose_name='CréditTEST restant'),
            preserve_default=True,
        ),
    ]
