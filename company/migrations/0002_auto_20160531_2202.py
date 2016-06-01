# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cities', '__first__'),
        ('company', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Industry',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=120, unique=True, null=True, blank=True)),
                ('is_primary', models.BooleanField(default=True)),
                ('parent', models.ForeignKey(blank=True, to='company.Industry', null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='auditor',
            name='address',
        ),
        migrations.RemoveField(
            model_name='producer',
            name='address',
        ),
        migrations.RemoveField(
            model_name='recycler',
            name='address',
        ),
        migrations.AddField(
            model_name='auditor',
            name='city',
            field=models.ForeignKey(blank=True, to='cities.City', null=True),
        ),
        migrations.AddField(
            model_name='auditor',
            name='city_text',
            field=models.CharField(max_length=120, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='auditor',
            name='country',
            field=models.ForeignKey(blank=True, to='cities.Country', null=True),
        ),
        migrations.AddField(
            model_name='auditor',
            name='phone_number',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='auditor',
            name='raw_address',
            field=models.CharField(max_length=300, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='auditor',
            name='state',
            field=models.ForeignKey(blank=True, to='cities.Region', null=True),
        ),
        migrations.AddField(
            model_name='auditor',
            name='street_address',
            field=models.CharField(max_length=300, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='auditor',
            name='zip_code',
            field=models.ForeignKey(blank=True, to='cities.PostalCode', null=True),
        ),
        migrations.AddField(
            model_name='producer',
            name='city',
            field=models.ForeignKey(blank=True, to='cities.City', null=True),
        ),
        migrations.AddField(
            model_name='producer',
            name='city_text',
            field=models.CharField(max_length=120, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='producer',
            name='country',
            field=models.ForeignKey(blank=True, to='cities.Country', null=True),
        ),
        migrations.AddField(
            model_name='producer',
            name='phone_number',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='producer',
            name='raw_address',
            field=models.CharField(max_length=300, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='producer',
            name='state',
            field=models.ForeignKey(blank=True, to='cities.Region', null=True),
        ),
        migrations.AddField(
            model_name='producer',
            name='street_address',
            field=models.CharField(max_length=300, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='producer',
            name='zip_code',
            field=models.ForeignKey(blank=True, to='cities.PostalCode', null=True),
        ),
        migrations.AddField(
            model_name='recycler',
            name='city',
            field=models.ForeignKey(blank=True, to='cities.City', null=True),
        ),
        migrations.AddField(
            model_name='recycler',
            name='city_text',
            field=models.CharField(max_length=120, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='recycler',
            name='country',
            field=models.ForeignKey(blank=True, to='cities.Country', null=True),
        ),
        migrations.AddField(
            model_name='recycler',
            name='phone_number',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='recycler',
            name='raw_address',
            field=models.CharField(max_length=300, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='recycler',
            name='state',
            field=models.ForeignKey(blank=True, to='cities.Region', null=True),
        ),
        migrations.AddField(
            model_name='recycler',
            name='street_address',
            field=models.CharField(max_length=300, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='recycler',
            name='zip_code',
            field=models.ForeignKey(blank=True, to='cities.PostalCode', null=True),
        ),
        migrations.AlterField(
            model_name='producer',
            name='industry',
            field=models.ForeignKey(blank=True, to='company.Industry', null=True),
        ),
    ]
