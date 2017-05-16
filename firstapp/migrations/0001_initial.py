# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CityMaster',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=120)),
                ('lastDateTimeModified', models.DateTimeField()),
                ('lastModifiedBy', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='CreateOrder',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('mobile', models.BigIntegerField(null=True, blank=True)),
                ('no_of_cloths', models.IntegerField()),
                ('house_no', models.CharField(max_length=250)),
                ('pin_code', models.BigIntegerField()),
                ('city', models.ForeignKey(to='firstapp.CityMaster', null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='StateMaster',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=120)),
                ('lastDateTimeModified', models.DateTimeField()),
                ('lastModifiedBy', models.CharField(max_length=120)),
            ],
        ),
        migrations.AddField(
            model_name='createorder',
            name='state',
            field=models.ForeignKey(to='firstapp.StateMaster', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='citymaster',
            name='state_name',
            field=models.ForeignKey(to='firstapp.StateMaster', null=True, blank=True),
        ),
    ]
