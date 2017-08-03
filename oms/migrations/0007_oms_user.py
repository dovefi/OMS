# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-03 02:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oms', '0006_auto_20170802_1924'),
    ]

    operations = [
        migrations.CreateModel(
            name='Oms_user',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(help_text='user name', max_length=11)),
                ('user_password', models.CharField(help_text='user password', max_length=15)),
                ('user_email', models.CharField(help_text='user email', max_length=30)),
                ('user_create_time', models.DateTimeField(help_text='user create time')),
            ],
        ),
    ]