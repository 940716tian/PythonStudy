# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-10-23 17:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app02', '0002_auto_20181023_1541'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, verbose_name='商品名字')),
                ('barcode', models.CharField(max_length=13, null=True, verbose_name='条码')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app02.Category')),
            ],
        ),
    ]
