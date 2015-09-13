# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_auto_20150912_2124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='log',
            name='is_deleted',
            field=models.NullBooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='log',
            name='is_read',
            field=models.NullBooleanField(default=False),
        ),
    ]
