# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-12-09 00:20
from __future__ import unicode_literals

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [("hordak", "0004_auto_20161113_1932")]

    operations = [
        migrations.AddField(
            model_name="account",
            name="currencies",
            field=django.contrib.postgres.fields.ArrayField(
                base_field=models.CharField(max_length=3),
                db_index=True,
                default=["EUR"],
                size=None,
            ),
            preserve_default=False,
        )
    ]
