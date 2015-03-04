# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='website',
            field=models.URLField(blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user',
            name='facebook',
            field=models.CharField(blank=True, max_length=200),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user',
            name='googleplus',
            field=models.CharField(blank=True, max_length=200),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user',
            name='instagram',
            field=models.CharField(blank=True, max_length=200),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user',
            name='twitter',
            field=models.CharField(blank=True, max_length=200),
            preserve_default=True,
        ),
    ]
