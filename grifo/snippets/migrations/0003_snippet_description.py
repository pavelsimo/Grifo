# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0002_auto_20150628_0731'),
    ]

    operations = [
        migrations.AddField(
            model_name='snippet',
            name='description',
            field=models.TextField(max_length=10000, verbose_name='Description', blank=True),
        ),
    ]
