# Generated by Django 4.1.2 on 2022-10-27 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maglumat', '0005_ishgarler_balnoy'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ishgarler',
            name='balnoy',
            field=models.BooleanField(default=False),
        ),
    ]
