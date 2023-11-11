# Generated by Django 3.2 on 2023-10-26 04:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('diplom', '0073_alter_ishgarler_barkod_surat'),
    ]

    operations = [
        migrations.CreateModel(
            name='Talyplar',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('at', models.CharField(max_length=100)),
                ('gelen_wagty', models.JSONField()),
                ('barkod_san', models.DecimalField(decimal_places=0, max_digits=13)),
                ('barkod_surat', models.ImageField(upload_to='barcode_img/')),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Toparlar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('san', models.IntegerField(default=0)),
                ('Topar_at', models.CharField(max_length=50)),
            ],
            options={
                'ordering': ['Topar_at'],
            },
        ),
        # migrations.RenameModel(
        #     old_name='Dinleyji_Gunler',
        #     new_name='Talyp_Gunler',
        # ),
        # migrations.RemoveField(
        #     model_name='dinleyjiler',
        #     name='kurs',
        # ),
        # migrations.DeleteModel(
        #     name='Isgar_Gunler',
        # ),
        # migrations.RemoveField(
        #     model_name='ishgarler',
        #     name='balnoy_gornush',
        # ),
        migrations.RemoveField(
            model_name='ishgarler',
            name='wezipe',
        ),
        # migrations.DeleteModel(
        #     name='Dinleyjiler',
        # ),
        migrations.DeleteModel(
            name='Ishgarler',
        ),
        # migrations.DeleteModel(
        #     name='Kurslar',
        # ),
        # migrations.DeleteModel(
        #     name='Rugsatlar',
        # ),
        migrations.DeleteModel(
            name='Wezipeler',
        ),
        migrations.AddField(
            model_name='talyplar',
            name='topar',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='degisli', to='diplom.toparlar'),
        ),
    ]