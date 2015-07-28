# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0015_auto_20150728_1623'),
    ]

    operations = [
        migrations.AddField(
            model_name='frontpageblurb',
            name='order_affinity',
            field=models.PositiveSmallIntegerField(default=5, help_text=b'Please specify how far the down the page it should be rendered, starting at 1'),
        ),
    ]
