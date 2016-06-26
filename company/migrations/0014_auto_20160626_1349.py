# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0013_load_waste_types'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductBatchEph',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('product_batch', models.OneToOneField(to='company.ProductBatch')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='RecAudPair',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('auditor', models.ForeignKey(to='company.Auditor')),
                ('recycler', models.ForeignKey(to='company.Recycler')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='productbatcheph',
            name='rec_aud_pairs',
            field=models.ManyToManyField(to='company.RecAudPair', blank=True),
        ),
    ]
