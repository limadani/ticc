# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-02-06 08:50
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('website', '0013_auto_20170206_0250'),
    ]

    operations = [
        migrations.AddField(
            model_name='matchscore',
            name='responsible',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
