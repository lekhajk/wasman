# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cities', '__first__'),
        ('company', '0005_auto_20160615_0625'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dismantler',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=120)),
                ('website', models.URLField(null=True, blank=True)),
                ('city_text', models.CharField(max_length=120, null=True, blank=True)),
                ('raw_address', models.CharField(max_length=300, null=True, blank=True)),
                ('street_address', models.CharField(max_length=300, null=True, blank=True)),
                ('phone_number', models.CharField(max_length=50, null=True, blank=True)),
                ('city', models.ForeignKey(blank=True, to='cities.City', null=True)),
                ('country', models.ForeignKey(blank=True, to='cities.Country', null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Producer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=120)),
                ('website', models.URLField(null=True, blank=True)),
                ('city_text', models.CharField(max_length=120, null=True, blank=True)),
                ('raw_address', models.CharField(max_length=300, null=True, blank=True)),
                ('street_address', models.CharField(max_length=300, null=True, blank=True)),
                ('phone_number', models.CharField(max_length=50, null=True, blank=True)),
                ('is_extended_producer', models.BooleanField(default=False)),
                ('type', models.CharField(blank=True, max_length=2, null=True, choices=[(b're', b'Retailer'), (b'et', b'Etailer'), (b'de', b'Dealer')])),
                ('city', models.ForeignKey(blank=True, to='cities.City', null=True)),
                ('country', models.ForeignKey(blank=True, to='cities.Country', null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Refurbisher',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=120)),
                ('website', models.URLField(null=True, blank=True)),
                ('city_text', models.CharField(max_length=120, null=True, blank=True)),
                ('raw_address', models.CharField(max_length=300, null=True, blank=True)),
                ('street_address', models.CharField(max_length=300, null=True, blank=True)),
                ('phone_number', models.CharField(max_length=50, null=True, blank=True)),
                ('city', models.ForeignKey(blank=True, to='cities.City', null=True)),
                ('country', models.ForeignKey(blank=True, to='cities.Country', null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='WasteType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=120)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RenameField(
            model_name='product',
            old_name='producer',
            new_name='manufacturer',
        ),
        migrations.AddField(
            model_name='producttype',
            name='code',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='refurbisher',
            name='product_types',
            field=models.ManyToManyField(to='company.ProductType'),
        ),
        migrations.AddField(
            model_name='refurbisher',
            name='state',
            field=models.ForeignKey(blank=True, to='cities.Region', null=True),
        ),
        migrations.AddField(
            model_name='refurbisher',
            name='zip_code',
            field=models.ForeignKey(blank=True, to='cities.PostalCode', null=True),
        ),
        migrations.AddField(
            model_name='producer',
            name='products',
            field=models.ManyToManyField(to='company.Product'),
        ),
        migrations.AddField(
            model_name='producer',
            name='state',
            field=models.ForeignKey(blank=True, to='cities.Region', null=True),
        ),
        migrations.AddField(
            model_name='producer',
            name='zip_code',
            field=models.ForeignKey(blank=True, to='cities.PostalCode', null=True),
        ),
        migrations.AddField(
            model_name='dismantler',
            name='product_types',
            field=models.ManyToManyField(to='company.ProductType'),
        ),
        migrations.AddField(
            model_name='dismantler',
            name='state',
            field=models.ForeignKey(blank=True, to='cities.Region', null=True),
        ),
        migrations.AddField(
            model_name='dismantler',
            name='zip_code',
            field=models.ForeignKey(blank=True, to='cities.PostalCode', null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='waste_types',
            field=models.ManyToManyField(to='company.WasteType'),
        ),
    ]
