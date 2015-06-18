# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StaticPage',
            fields=[
                ('title', models.CharField(help_text=b'The title to appear at the top of the page', max_length=50)),
                ('content', models.TextField(help_text=b'The page content you wish to display', blank=True)),
                ('url', models.CharField(help_text=b"The url to be matched.  Eg. '/about-us/'.  Be sure to include to front and end /'s", max_length=50, serialize=False, primary_key=True)),
                ('template', models.CharField(default=b'staticpage.html', help_text=b'If using a different template, you can override it with this', max_length=50)),
            ],
        ),
    ]
