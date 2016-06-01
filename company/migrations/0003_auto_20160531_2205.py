# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.core.management import call_command


def load_fixture(apps, schema_editor):
    fixture = 'industries.json'
    call_command('loaddata', fixture, app_label='company')


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0002_auto_20160531_2202'),
    ]

    operations = [ migrations.RunPython(load_fixture, migrations.RunPython.noop),
    ]
