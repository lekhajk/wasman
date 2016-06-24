# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cities', '__first__'),
        ('company', '0008_auto_20160621_1747'),
    ]

    operations = [
        migrations.CreateModel(
            name='GovernmentAgency',
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
        migrations.RemoveField(
            model_name='governmentageny',
            name='city',
        ),
        migrations.RemoveField(
            model_name='governmentageny',
            name='country',
        ),
        migrations.RemoveField(
            model_name='governmentageny',
            name='industry',
        ),
        migrations.RemoveField(
            model_name='governmentageny',
            name='state',
        ),
        migrations.RemoveField(
            model_name='governmentageny',
            name='zip_code',
        ),
        migrations.DeleteModel(
            name='GovernmentAgeny',
        ),
    ]
