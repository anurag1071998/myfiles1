# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('firstapp', '0002_auto_20170507_2242'),
    ]

    operations = [
        migrations.CreateModel(
            name='Register',
            fields=[
                ('userId', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('date_of_birth', models.DateField()),
                ('phone', models.BigIntegerField(null=True, blank=True)),
                ('email', models.EmailField(max_length=254)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL, null=True, blank=True)),
            ],
        ),
    ]
