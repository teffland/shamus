# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0012_auto_20150626_0215'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sliderimage',
            name='height',
            field=models.IntegerField(default=500, help_text=b'Ideally, height is 9/16(width) naturally; it will be stretched to this ratio automatically'),
        ),
        migrations.AlterField(
            model_name='sliderimage',
            name='image',
            field=models.ImageField(help_text=b'An image to be displayed in the slider', height_field=b'height', width_field=b'width', upload_to=b'image-slider'),
        ),
        migrations.AlterField(
            model_name='sliderimage',
            name='width',
            field=models.IntegerField(default=500, help_text=b'Suggested keep 16:9 aspect ratio for width:height'),
        ),
    ]
