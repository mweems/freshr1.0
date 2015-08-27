# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('newsFeed', '0009_auto_20150823_1309'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='date',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2015, 8, 27, 11, 38, 36, 268650, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
