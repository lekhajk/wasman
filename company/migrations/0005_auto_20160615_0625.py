# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cities', '__first__'),
        ('company', '0004_auto_20160606_1917'),
    ]

    operations = [
        migrations.CreateModel(
            name='Manufacturer',
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
                ('stock_ticker', models.CharField(max_length=120)),
                ('city', models.ForeignKey(blank=True, to='cities.City', null=True)),
                ('country', models.ForeignKey(blank=True, to='cities.Country', null=True)),
                ('industry', models.ForeignKey(blank=True, to='company.Industry', null=True)),
                ('state', models.ForeignKey(blank=True, to='cities.Region', null=True)),
                ('zip_code', models.ForeignKey(blank=True, to='cities.PostalCode', null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='producer',
            name='city',
        ),
        migrations.RemoveField(
            model_name='producer',
            name='country',
        ),
        migrations.RemoveField(
            model_name='producer',
            name='industry',
        ),
        migrations.RemoveField(
            model_name='producer',
            name='state',
        ),
        migrations.RemoveField(
            model_name='producer',
            name='zip_code',
        ),
        migrations.AlterField(
            model_name='product',
            name='producer',
            field=models.ForeignKey(to='company.Manufacturer'),
        ),
        migrations.DeleteModel(
            name='Producer',
        ),
    ]
