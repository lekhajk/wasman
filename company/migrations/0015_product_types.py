# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.core.management import call_command


def load_fixture(apps, schema_editor):
    fixture = 'product_types.json'
    call_command('loaddata', fixture, app_label='company')

class Migration(migrations.Migration):

    dependencies = [
        ('company', '0014_auto_20160626_1349'),
    ]

    operations = [ migrations.RunPython(load_fixture, migrations.RunPython.noop),
    ]
