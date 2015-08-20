# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsFeed', '0002_auto_20150819_1103'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='image',
            field=models.FileField(default='', upload_to=''),
        ),
    ]
