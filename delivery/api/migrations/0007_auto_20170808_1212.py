# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-08 12:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_auto_20170808_1209'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='promo_code',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.Promo'),
        ),
    ]
