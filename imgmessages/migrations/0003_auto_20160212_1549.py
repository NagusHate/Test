# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-12 12:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imgmessages', '0002_auto_20160212_1546'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imgmessage',
            name='img',
            field=models.ImageField(upload_to='img'),
        ),
    ]