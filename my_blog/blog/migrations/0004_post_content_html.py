# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-05-03 09:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20190503_1136'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='content_html',
            field=models.TextField(blank=True, editable=False, null=True, verbose_name='正文html代码'),
        ),
    ]
