# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-11-29 02:31
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0002_auto_20171128_1629'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='shuoshi',
            options={'managed': False, 'verbose_name': '硕士Offer', 'verbose_name_plural': '硕士Offers'},
        ),
    ]
