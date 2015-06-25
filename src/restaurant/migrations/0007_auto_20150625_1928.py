# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0006_auto_20150623_2245'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemoption',
            name='price',
            field=models.DecimalField(help_text=b'How much the item costs', null=True, max_digits=6, decimal_places=2, blank=True),
        ),
    ]
