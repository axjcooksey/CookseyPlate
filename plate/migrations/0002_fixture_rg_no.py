# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-12-11 21:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plate', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='fixture',
            name='rg_no',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
