# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-02 10:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('oms', '0003_auto_20170802_1835'),
    ]

    operations = [
        migrations.AlterField(
            model_name='module_list',
            name='module_caption',
            field=models.CharField(help_text='module caption', max_length=255),
        ),
        migrations.AlterField(
            model_name='module_list',
            name='module_extend',
            field=models.CharField(help_text='module extend', max_length=2000),
        ),
        migrations.AlterField(
            model_name='module_list',
            name='module_name',
            field=models.CharField(help_text='module name', max_length=20),
        ),
        migrations.AlterField(
            model_name='server_app_categ',
            name='app_categ_name',
            field=models.CharField(help_text='name of service application category ', max_length=30),
        ),
        migrations.AlterField(
            model_name='server_app_categ',
            name='server_fun_categ',
            field=models.ForeignKey(help_text='foreign key,service function id,delete cascade ', on_delete=django.db.models.deletion.CASCADE, to='oms.Server_fun_categ'),
        ),
        migrations.AlterField(
            model_name='server_fun_categ',
            name='server_categ_name',
            field=models.CharField(help_text='name of service function category ', max_length=20),
        ),
        migrations.AlterField(
            model_name='server_list',
            name='server_app_categ',
            field=models.ForeignKey(help_text='id of service application category', on_delete=django.db.models.deletion.CASCADE, to='oms.Server_app_categ'),
        ),
        migrations.AlterField(
            model_name='server_list',
            name='server_lip',
            field=models.CharField(help_text='server inner network ip', max_length=12),
        ),
        migrations.AlterField(
            model_name='server_list',
            name='server_name',
            field=models.CharField(help_text='server name', max_length=13),
        ),
        migrations.AlterField(
            model_name='server_list',
            name='server_op',
            field=models.CharField(help_text='OS of server', max_length=10),
        ),
        migrations.AlterField(
            model_name='server_list',
            name='server_wip',
            field=models.CharField(help_text='server public network ip', max_length=15),
        ),
    ]