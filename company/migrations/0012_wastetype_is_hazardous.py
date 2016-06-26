# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0011_recyclers_seed_list'),
    ]

    operations = [
        migrations.AddField(
            model_name='wastetype',
            name='is_hazardous',
            field=models.BooleanField(default=False),
        ),
    ]
