# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0005_auto_20150623_2203'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemoption',
            name='description',
            field=models.CharField(help_text=b'The description text', max_length=255, blank=True),
        ),
        migrations.AlterField(
            model_name='itemoption',
            name='price_suffix',
            field=models.CharField(help_text=b'Text to be displayed after price', max_length=10, blank=True),
        ),
        migrations.AlterField(
            model_name='menucategory',
            name='order_affinity',
            field=models.PositiveSmallIntegerField(default=5, help_text=b'Please specify how far down the menu it should be rendered, starting at 1'),
        ),
        migrations.AlterField(
            model_name='menuitem',
            name='price_suffix',
            field=models.CharField(help_text=b'Text to be displayed after price', max_length=10, blank=True),
        ),
        migrations.AlterField(
            model_name='sliderimage',
            name='order_affinity',
            field=models.PositiveSmallIntegerField(default=5, help_text=b'Please specify how far the down the slider it should be rendered, starting at 1'),
        ),
    ]
