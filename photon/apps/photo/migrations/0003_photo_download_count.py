# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0002_photo_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='download_count',
            field=models.PositiveIntegerField(default=0),
            preserve_default=True,
        ),
    ]
