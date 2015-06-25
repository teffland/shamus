# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0009_auto_20150625_2246'),
    ]

    operations = [
        migrations.AddField(
            model_name='menuitem',
            name='published',
            field=models.BooleanField(default=True),
        ),
    ]
