# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-10-24 22:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app03plus', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Stu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app03plus.Grade')),
            ],
        ),
        migrations.AlterField(
            model_name='person',
            name='idcard',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='app03plus.IdCard'),
        ),
    ]
