# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_auto_20150912_2204'),
    ]

    operations = [
        migrations.AlterField(
            model_name='log',
            name='article',
            field=models.ForeignKey(to='news.Article'),
        ),
        migrations.AlterField(
            model_name='log',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
