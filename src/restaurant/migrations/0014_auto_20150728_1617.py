# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0013_auto_20150626_1627'),
    ]

    operations = [
        migrations.CreateModel(
            name='FrontPageBlurb',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('heading', models.CharField(help_text=b'The title to appear at the top of the blurb', max_length=50)),
                ('comment', models.CharField(help_text=b'An afterthought to appear next to the heading at the top of the blurb', max_length=50)),
                ('content', models.TextField(help_text=b'The main content of the blurb', blank=True)),
                ('image', models.ImageField(help_text=b'An image to be displayed in the featurette', height_field=b'height', width_field=b'width', upload_to=b'featurette-images')),
                ('published', models.BooleanField(default=True)),
            ],
        ),
        migrations.AlterField(
            model_name='sliderimage',
            name='height',
            field=models.IntegerField(default=576, help_text=b'Ideally, height is 9/16(width) naturally; it will be stretched to this ratio automatically'),
        ),
        migrations.AlterField(
            model_name='sliderimage',
            name='width',
            field=models.IntegerField(default=1024, help_text=b'Suggested keep 16:9 aspect ratio for width:height'),
        ),
    ]
