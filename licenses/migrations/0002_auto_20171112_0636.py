# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-12 14:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('licenses', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='license',
            name='li_current_assesments',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='license',
            name='li_current_staff',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='license',
            name='li_current_students',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='license',
            name='li_max_assesments',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='license',
            name='li_max_staff',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='license',
            name='li_max_students',
            field=models.IntegerField(default=0),
        ),
    ]