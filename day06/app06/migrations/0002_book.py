# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-10-29 13:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app06', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('icon', models.ImageField(upload_to='icons')),
            ],
        ),
    ]
