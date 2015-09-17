# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsFeed', '0012_auto_20150917_2028'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='post_date',
            new_name='date',
        ),
    ]
