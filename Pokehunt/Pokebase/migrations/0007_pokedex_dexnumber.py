# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-09-11 17:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pokebase', '0006_pokedex_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='pokedex',
            name='dexnumber',
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]
