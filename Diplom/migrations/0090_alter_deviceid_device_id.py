# Generated by Django 4.1.2 on 2024-02-29 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diplom', '0089_alter_deviceid_device_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deviceid',
            name='device_id',
            field=models.CharField(max_length=10485760),
        ),
    ]