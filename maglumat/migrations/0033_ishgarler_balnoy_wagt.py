# Generated by Django 4.1.2 on 2022-11-07 09:34

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maglumat', '0032_remove_ishgarler_balnoy_wagt'),
    ]

    operations = [
        migrations.AddField(
            model_name='ishgarler',
            name='balnoy_wagt',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=100), default=list, size=None),
        ),
    ]
