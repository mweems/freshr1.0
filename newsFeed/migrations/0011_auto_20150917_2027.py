# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsFeed', '0010_item_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='item',
            name='phone',
            field=models.CharField(max_length=200),
        ),
    ]
