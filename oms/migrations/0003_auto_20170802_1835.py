# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-02 10:35
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oms', '0002_auto_20170802_1734'),
    ]

    operations = [
        migrations.RenameField(
            model_name='module_list',
            old_name='models_extend',
            new_name='module_extend',
        ),
    ]
