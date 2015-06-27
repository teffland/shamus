# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0011_auto_20150626_0208'),
    ]

    operations = [
        migrations.AddField(
            model_name='sliderimage',
            name='height',
            field=models.IntegerField(default=500),
        ),
        migrations.AddField(
            model_name='sliderimage',
            name='width',
            field=models.IntegerField(default=500),
        ),
        migrations.AlterField(
            model_name='sliderimage',
            name='image',
            field=models.ImageField(help_text=b'An image to be displayed in the slider', height_field=models.IntegerField(default=500), width_field=models.IntegerField(default=500), upload_to=b'img'),
        ),
    ]
