# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0010_menuitem_published'),
    ]

    operations = [
        migrations.AddField(
            model_name='sliderimage',
            name='published',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='menutype',
            name='end_time',
            field=models.TimeField(help_text=b'What time the the menu is no longer served. Format: 1 pm is 13:00:00'),
        ),
        migrations.AlterField(
            model_name='menutype',
            name='start_time',
            field=models.TimeField(help_text=b'What time the menu is available to be served. Format: 1 pm is 13:00:00'),
        ),
        migrations.AlterField(
            model_name='sliderimage',
            name='image',
            field=models.ImageField(help_text=b'An image to be displayed in the slider', upload_to=b''),
        ),
    ]
