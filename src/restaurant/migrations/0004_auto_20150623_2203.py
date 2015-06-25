# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0003_auto_20150623_2139'),
    ]

    operations = [
        migrations.CreateModel(
            name='ItemOption',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.TextField(help_text=b'The description text', blank=True)),
                ('price', models.DecimalField(help_text=b'How much the item costs', max_digits=6, decimal_places=2, blank=True)),
                ('price_suffix', models.TextField(help_text=b'Text to be displayed after price', blank=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='menuitem',
            name='description',
        ),
        migrations.AddField(
            model_name='menuitem',
            name='price_suffix',
            field=models.TextField(help_text=b'Text to be displayed after price', blank=True),
        ),
        migrations.AlterField(
            model_name='sliderimage',
            name='order_affinity',
            field=models.SmallIntegerField(default=5, help_text=b'Please specify how far the down the slider it should be rendered, starting at 1'),
        ),
        migrations.AddField(
            model_name='itemoption',
            name='parent_item',
            field=models.ForeignKey(to='restaurant.MenuItem'),
        ),
    ]
