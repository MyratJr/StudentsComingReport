# Generated by Django 4.1.2 on 2023-10-26 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diplom', '0078_alter_talyplar_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='talyplar',
            name='ID_NO',
            field=models.IntegerField(default=203124),
            preserve_default=False,
        ),
    ]
