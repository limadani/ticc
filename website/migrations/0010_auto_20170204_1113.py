# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-02-04 13:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0009_auto_20170204_1105'),
    ]

    operations = [
        migrations.RenameField(
            model_name='match',
            old_name='local',
            new_name='location',
        ),
        migrations.AlterField(
            model_name='match',
            name='competition',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='matches', to='website.Competition'),
        ),
    ]