# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('auther', models.CharField(max_length=200)),
                ('publication_date', models.DateTimeField(verbose_name=b'date published')),
                ('category', models.CharField(max_length=100)),
                ('hero_image', models.ImageField(upload_to=b'images/')),
                ('body', models.TextField()),
            ],
        ),
    ]
