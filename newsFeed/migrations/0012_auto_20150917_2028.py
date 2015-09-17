# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsFeed', '0011_auto_20150917_2027'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='date',
            new_name='post_date',
        ),
    ]
