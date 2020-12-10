# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('itemid', models.IntegerField()),
                ('itemname', models.CharField(max_length=50)),
                ('ccode', models.CharField(max_length=50)),
                ('bid', models.CharField(max_length=50)),
                ('price', models.FloatField(max_length=20)),
                ('des', models.CharField(max_length=50)),
                ('qty', models.IntegerField()),
                ('image', models.FileField(upload_to=b'pictures')),
            ],
            options={
                'db_table': 'item',
            },
        ),
    ]
