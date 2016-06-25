# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0009_auto_20160624_0903'),
    ]

    operations = [
        migrations.AddField(
            model_name='recycler',
            name='capacity',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
