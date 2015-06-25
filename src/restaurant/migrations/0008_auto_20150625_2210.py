# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0007_auto_20150625_1928'),
    ]

    operations = [
        migrations.RenameField(
            model_name='itemoption',
            old_name='price_suffix',
            new_name='price_prefix',
        ),
        migrations.RenameField(
            model_name='menuitem',
            old_name='price_suffix',
            new_name='price_prefix',
        ),
    ]
