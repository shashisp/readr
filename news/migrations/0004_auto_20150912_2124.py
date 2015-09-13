# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('news', '0003_auto_20150910_1952'),
    ]

    operations = [
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('is_read', models.BooleanField(default=False)),
                ('is_deleted', models.BooleanField(default=False)),
                ('article', models.OneToOneField(to='news.Article')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='deletelog',
            name='article',
        ),
        migrations.RemoveField(
            model_name='deletelog',
            name='user',
        ),
        migrations.RemoveField(
            model_name='readlog',
            name='article',
        ),
        migrations.RemoveField(
            model_name='readlog',
            name='user',
        ),
        migrations.DeleteModel(
            name='DeleteLog',
        ),
        migrations.DeleteModel(
            name='ReadLog',
        ),
    ]
