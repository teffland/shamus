# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0004_auto_20150623_2203'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menucategory',
            name='order_affinity',
            field=models.SmallIntegerField(default=5, help_text=b'Please specify how far down the menu it should be rendered, starting at 1'),
        ),
    ]
