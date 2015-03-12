# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_remove_user_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='facebook',
            field=models.URLField(blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user',
            name='googleplus',
            field=models.URLField(blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user',
            name='instagram',
            field=models.URLField(blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user',
            name='twitter',
            field=models.URLField(blank=True),
            preserve_default=True,
        ),
    ]
