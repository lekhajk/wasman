# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('cities', '__first__'),
        ('company', '0003_auto_20160531_2205'),
    ]

    operations = [
        migrations.CreateModel(
            name='GovernmentAgeny',
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
                ('industry', models.ForeignKey(blank=True, to='company.Industry', null=True)),
                ('state', models.ForeignKey(blank=True, to='cities.Region', null=True)),
                ('zip_code', models.ForeignKey(blank=True, to='cities.PostalCode', null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ProductBatch',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('batch_id', models.CharField(max_length=120)),
                ('auditor', models.ForeignKey(blank=True, to='company.Auditor', null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ProductType',
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
        migrations.AddField(
            model_name='product',
            name='auditors',
            field=models.ManyToManyField(to='company.Auditor'),
        ),
        migrations.AddField(
            model_name='product',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2016, 6, 6, 19, 16, 53, 961104, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='recyclers',
            field=models.ManyToManyField(to='company.Recycler'),
        ),
        migrations.AddField(
            model_name='product',
            name='updated_on',
            field=models.DateTimeField(default=datetime.datetime(2016, 6, 6, 19, 17, 0, 276551, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='type',
            field=models.ForeignKey(blank=True, to='company.ProductType', null=True),
        ),
        migrations.AddField(
            model_name='productbatch',
            name='product',
            field=models.ForeignKey(to='company.Product'),
        ),
        migrations.AddField(
            model_name='productbatch',
            name='recycler',
            field=models.ForeignKey(blank=True, to='company.Recycler', null=True),
        ),
        migrations.AddField(
            model_name='recycler',
            name='recyclable_types',
            field=models.ManyToManyField(to='company.ProductType'),
        ),
    ]
