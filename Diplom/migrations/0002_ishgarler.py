# Generated by Django 4.1.2 on 2022-10-20 14:59

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('diplom', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ishgarler',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('at', models.CharField(max_length=100)),
                ('gelen_wagty', models.JSONField()),
                ('giden_wagty', models.JSONField()),
                ('is_bashlayar', models.TimeField(default=datetime.time(9, 0))),
                ('is_gutaryar', models.TimeField(default=datetime.time(17, 0))),
                ('obed_bashlayar', models.TimeField(default=datetime.time(13, 0))),
                ('obed_gutaryar', models.TimeField(default=datetime.time(14, 0))),
                ('barkod_san', models.CharField(max_length=15)),
                ('barkod_surat', models.ImageField(blank=True, upload_to='barcode_img/')),
                ('wezipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='diplom.wezipeler')),
            ],
            options={
                'ordering': ['id'],
            },
        ),
    ]
