# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-02 11:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oms', '0005_auto_20170802_1923'),
    ]

    operations = [
        migrations.AlterField(
            model_name='server_history',
            name='history_id',
            field=models.IntegerField(help_text='history id'),
        ),
    ]