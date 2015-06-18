# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MenuCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(help_text=b'The name of a menu category, eg. Appetizers, Salads, or Sandwiches', max_length=50)),
                ('description', models.TextField(help_text=b'The description to be displayed on the menu', blank=True)),
                ('order_affinity', models.PositiveSmallIntegerField(default=5, help_text=b'Please specify how far down the menu it should be rendered, starting at 1')),
            ],
        ),
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(help_text=b'The name of a menu item, eg. Lobster Bisque', max_length=50)),
                ('description', models.TextField(help_text=b'The description to be displayed when scrolling over the item', blank=True)),
                ('price', models.DecimalField(help_text=b'How much the item costs', max_digits=6, decimal_places=2)),
                ('image', models.ImageField(upload_to=b'', width_field=b'width', height_field=b'height', blank=True, help_text=b'Please upload an image of the dish')),
                ('menu_category', models.ForeignKey(to='restaurant.MenuCategory')),
            ],
        ),
        migrations.CreateModel(
            name='MenuType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(help_text=b'The name of a menu type, eg. Lunch, Dinner', max_length=50)),
                ('description', models.TextField(help_text=b'The description to be displayed when scrolling over the menu', blank=True)),
                ('start_time', models.TimeField(help_text=b'What time the menu is available to be served')),
                ('end_time', models.TimeField(help_text=b'What time the the menu is no longer served')),
            ],
        ),
        migrations.CreateModel(
            name='SliderImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(help_text=b'The name of a image', max_length=50)),
                ('caption', models.TextField(help_text=b'The caption to be displayed overlaying the image', blank=True)),
                ('image', models.ImageField(help_text=b'An image to be displayed in the slider', height_field=b'height', width_field=b'width', upload_to=b'')),
                ('link', models.URLField(help_text=b'Please provide a link to the part of the site the image is representing', blank=True)),
                ('order_affinity', models.PositiveSmallIntegerField(default=5, help_text=b'Please specify how far the down the slider it should be rendered, starting at 1')),
            ],
        ),
        migrations.AddField(
            model_name='menuitem',
            name='menu_types',
            field=models.ManyToManyField(to='restaurant.MenuType'),
        ),
    ]
