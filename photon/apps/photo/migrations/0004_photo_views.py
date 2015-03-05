# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0003_photo_download_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='views',
            field=models.PositiveIntegerField(default=0),
            preserve_default=True,
        ),
    ]
