# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('hn_id', models.IntegerField()),
                ('url', models.URLField()),
                ('hn_url', models.URLField()),
                ('posted_on', models.CharField(max_length=100)),
                ('up_votes', models.IntegerField()),
                ('comments', models.IntegerField()),
            ],
        ),
    ]
