# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.CharField(max_length=20, serialize=False, primary_key=True)),
                ('cuz_ID', models.CharField(max_length=20)),
                ('classTime', models.TextField()),
                ('classHour', models.IntegerField()),
                ('class_capacity', models.IntegerField()),
                ('campus', models.CharField(max_length=20)),
                ('teacherID', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='classroom',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20)),
                ('type', models.CharField(default=b'classroom', max_length=20)),
                ('capacity', models.IntegerField()),
                ('campus', models.CharField(max_length=20)),
            ],
        ),
    ]
