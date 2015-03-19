# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_auto_20150311_2035'),
    ]

    operations = [
        migrations.CreateModel(
            name='TmpImage',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('image', models.ImageField(upload_to='tmp')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
