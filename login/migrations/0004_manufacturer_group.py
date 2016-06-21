# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from login.localsettings import manufacturer_group_name
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType

def create_manufacturer_group(apps, schema_editor):
    g = Group.objects.create(name=manufacturer_group_name)
    Product = apps.get_model('company', 'Product')
    ProductType = apps.get_model('company', 'ProductType')
    permissions = Permission.objects.filter(content_type__in=[ContentType.objects.get_for_model(Product),
                                                              ContentType.objects.get_for_model(ProductType),])
    for p in permissions:
        g.permissions.add(p)
    
class Migration(migrations.Migration):

    dependencies = [
        ('login', '0003_auto_20160620_1843'),
    ]

    operations = [ migrations.RunPython(create_manufacturer_group, migrations.RunPython.noop),
    ]
