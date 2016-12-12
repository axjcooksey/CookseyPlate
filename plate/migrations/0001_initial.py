# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-12-11 21:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fixture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('game_no', models.IntegerField()),
                ('round_no', models.IntegerField()),
                ('game_code', models.CharField(max_length=10)),
                ('game_day', models.CharField(max_length=10)),
                ('game_date', models.DateField()),
                ('game_time', models.TimeField()),
                ('time_slot', models.CharField(max_length=2)),
                ('game_state', models.CharField(max_length=4)),
                ('hmaw_status', models.CharField(max_length=2)),
                ('home_team', models.CharField(max_length=30)),
                ('ht_code', models.CharField(max_length=4)),
                ('away_team', models.CharField(max_length=30)),
                ('at_code', models.CharField(max_length=4)),
                ('ground_name', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Selection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('selected_team', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('family_username', models.CharField(max_length=30)),
                ('fav_team', models.CharField(max_length=30)),
            ],
        ),
    ]
