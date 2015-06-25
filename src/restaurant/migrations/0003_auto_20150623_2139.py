# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0002_staticpage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menuitem',
            name='menu_types',
        ),
        migrations.AddField(
            model_name='menucategory',
            name='menu_types',
            field=models.ManyToManyField(to='restaurant.MenuType'),
        ),
        migrations.RemoveField(
            model_name='menuitem',
            name='menu_category',
        ),
        migrations.AddField(
            model_name='menuitem',
            name='menu_category',
            field=models.ManyToManyField(to='restaurant.MenuCategory'),
        ),
        migrations.AlterField(
            model_name='staticpage',
            name='url',
            field=models.CharField(help_text=b"The url to be matched.  Eg. 'about-us/'.  Be sure to include the trailing / ", max_length=50, serialize=False, primary_key=True),
        ),
    ]
