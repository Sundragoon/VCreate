# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-09-11 02:49
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Pokebase', '0003_auto_20160911_0107'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trainer',
            name='trainer_name',
        ),
    ]
