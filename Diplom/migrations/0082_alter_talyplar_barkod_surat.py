# Generated by Django 4.1.2 on 2023-11-11 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diplom', '0081_rename_days_talyp_gunler_alter_talyp_gunler_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='talyplar',
            name='barkod_surat',
            field=models.ImageField(default=None, upload_to='barcode_img/'),
        ),
    ]
