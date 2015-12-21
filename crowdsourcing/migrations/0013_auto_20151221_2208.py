# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-21 22:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crowdsourcing', '0012_get_min_ratings_fn'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='parent',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='crowdsourcing.Project'),
        ),
        migrations.AlterField(
            model_name='project',
            name='is_prototype',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='name',
            field=models.CharField(default=b'Untitled Project', error_messages={b'required': b'Please enter the project name!'}, max_length=128),
        ),
    ]
