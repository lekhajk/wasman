# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.core.management import call_command


def load_fixture(apps, schema_editor):
    fixture = 'waste_types.json'
    call_command('loaddata', fixture, app_label='company')


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0012_wastetype_is_hazardous'),
    ]

    operations = [migrations.RunPython(load_fixture, migrations.RunPython.noop)
    ]
