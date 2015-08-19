# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsFeed', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='name',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='item',
            name='phone',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='item',
            name='text',
            field=models.TextField(default=''),
        ),
    ]
