# Generated by Django 4.1.2 on 2024-02-28 14:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('diplom', '0085_remove_talyplar_device_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='talyplar',
            name='device_id',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='diplom.deviceid'),
        ),
    ]
