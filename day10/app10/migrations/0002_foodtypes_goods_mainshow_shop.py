# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-11-05 12:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app10', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FoodTypes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('typeid', models.CharField(max_length=20)),
                ('typename', models.CharField(max_length=30)),
                ('childtypenames', models.CharField(max_length=255)),
                ('typesort', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'axf_foodtypes',
            },
        ),
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productid', models.CharField(max_length=20)),
                ('productimg', models.CharField(max_length=200)),
                ('productname', models.CharField(max_length=200, null=True)),
                ('productlongname', models.CharField(max_length=200)),
                ('isxf', models.BooleanField(default=0)),
                ('pmdesc', models.BooleanField(default=0)),
                ('specifics', models.CharField(max_length=20)),
                ('price', models.FloatField()),
                ('marketprice', models.FloatField()),
                ('categoryid', models.IntegerField()),
                ('childcid', models.IntegerField()),
                ('childcidname', models.CharField(max_length=10)),
                ('dealerid', models.CharField(max_length=20)),
                ('storenums', models.IntegerField(verbose_name='库存')),
                ('productnum', models.IntegerField(verbose_name='销量')),
            ],
            options={
                'db_table': 'axf_goods',
            },
        ),
        migrations.CreateModel(
            name='Mainshow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.CharField(max_length=251)),
                ('name', models.CharField(max_length=40)),
                ('trackid', models.CharField(max_length=30)),
                ('categoryid', models.CharField(max_length=100)),
                ('brandname', models.CharField(max_length=100)),
                ('img1', models.CharField(max_length=255)),
                ('childcid1', models.CharField(max_length=100)),
                ('productid1', models.CharField(max_length=100)),
                ('longname1', models.CharField(max_length=100)),
                ('price1', models.CharField(max_length=100)),
                ('marketprice1', models.CharField(max_length=100)),
                ('img2', models.CharField(max_length=255)),
                ('childcid2', models.CharField(max_length=100)),
                ('productid2', models.CharField(max_length=100)),
                ('longname2', models.CharField(max_length=100)),
                ('price2', models.CharField(max_length=100)),
                ('marketprice2', models.CharField(max_length=100)),
                ('img3', models.CharField(max_length=255)),
                ('childcid3', models.CharField(max_length=100)),
                ('productid3', models.CharField(max_length=100)),
                ('longname3', models.CharField(max_length=100)),
                ('price3', models.CharField(max_length=100)),
                ('marketprice3', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'axf_mainshow',
            },
        ),
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.CharField(max_length=251)),
                ('name', models.CharField(max_length=40)),
                ('trackid', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'axf_shop',
            },
        ),
    ]
