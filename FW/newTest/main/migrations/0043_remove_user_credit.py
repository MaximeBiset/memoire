# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0042_user_credit'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='credit',
        ),
    ]
