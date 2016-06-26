# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from login.localsettings import government_agency_group_name
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType


def create_ga_group(apps, schema_editor):
    g = Group.objects.create(name=government_agency_group_name)
    permission = Permission.objects.get(codename='change_productbatcheph')
    g.permissions.add(permission)
    

class Migration(migrations.Migration):

    dependencies = [
        ('login', '0005_userprofile_activation_key'),
    ]

    operations = [migrations.RunPython(create_ga_group, migrations.RunPython.noop),
    ]
