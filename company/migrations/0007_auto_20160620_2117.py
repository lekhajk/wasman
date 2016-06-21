# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0006_auto_20160615_1922'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='auditors',
            field=models.ManyToManyField(to='company.Auditor', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='manufacturer',
            field=models.ForeignKey(blank=True, to='company.Manufacturer', null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='recyclers',
            field=models.ManyToManyField(to='company.Recycler', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='waste_types',
            field=models.ManyToManyField(to='company.WasteType', null=True, blank=True),
        ),
    ]
