# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='createorder',
            name='username',
            field=models.CharField(max_length=25, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='createorder',
            name='no_of_cloths',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
