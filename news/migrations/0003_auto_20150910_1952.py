# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_deletelog_readlog'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='posted_on',
            field=models.DateTimeField(null=True),
        ),
    ]
