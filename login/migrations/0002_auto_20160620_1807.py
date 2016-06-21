# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='homepage',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='content_type',
            field=models.ForeignKey(blank=True, to='contenttypes.ContentType', null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='email',
            field=models.EmailField(max_length=254, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='object_id',
            field=models.PositiveIntegerField(null=True, blank=True),
        ),
    ]
