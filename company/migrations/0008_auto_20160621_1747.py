# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0007_auto_20160620_2117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='auditors',
            field=models.ManyToManyField(to='company.Auditor', blank=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='recyclers',
            field=models.ManyToManyField(to='company.Recycler', blank=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, blank=True, to='company.ProductType', null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='waste_types',
            field=models.ManyToManyField(to='company.WasteType', blank=True),
        ),
    ]
