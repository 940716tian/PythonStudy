# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-10-29 14:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app06', '0002_book'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='icon_url',
            field=models.CharField(max_length=251, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='icon',
            field=models.ImageField(null=True, upload_to='icons'),
        ),
    ]