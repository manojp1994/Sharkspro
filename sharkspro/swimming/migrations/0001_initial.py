# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('PostedName', models.CharField(max_length=30)),
                ('PostedMobile', models.CharField(max_length=15)),
                ('PostedReview', models.CharField(max_length=400)),
            ],
        ),
    ]
