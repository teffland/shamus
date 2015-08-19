# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0016_frontpageblurb_order_affinity'),
    ]

    operations = [
        migrations.CreateModel(
            name='MaintenanceMode',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('maintenance', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Site Configuration',
            },
        ),
    ]
