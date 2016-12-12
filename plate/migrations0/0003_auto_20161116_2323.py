# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-11-16 23:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plate', '0002_round1_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Selection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30)),
                ('round_no', models.IntegerField()),
                ('game_no', models.IntegerField()),
                ('selected_team', models.CharField(max_length=30)),
            ],
        ),
        migrations.DeleteModel(
            name='Round1',
        ),
    ]
