# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0014_auto_20150728_1617'),
    ]

    operations = [
        migrations.AddField(
            model_name='frontpageblurb',
            name='height',
            field=models.IntegerField(default=500, help_text=b"You don't need to change this (it adjusts automatically)"),
        ),
        migrations.AddField(
            model_name='frontpageblurb',
            name='width',
            field=models.IntegerField(default=500, help_text=b"You don't need to change this (it adjusts automatically)"),
        ),
        migrations.AlterField(
            model_name='frontpageblurb',
            name='comment',
            field=models.CharField(help_text=b'An afterthought to appear next to the heading at the top of the blurb', max_length=50, blank=True),
        ),
    ]
