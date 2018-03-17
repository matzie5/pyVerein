# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-03-17 15:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='account_type',
            field=models.CharField(choices=[('CRE', 'Creditor'), ('DEB', 'Debitor'), ('COS', 'Cost'), ('INC', 'Income')], default='COS', max_length=3),
        ),
    ]
