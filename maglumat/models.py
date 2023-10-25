from django.db import models
from django.db.models import JSONField
import datetime,barcode
from barcode.writer import ImageWriter
from io import BytesIO
from django.core.files import File
from django.contrib.postgres.fields import ArrayField
import django

class del_info_gun(models.Model):
    gun=models.CharField(max_length=10)

    def __str__(self):
        return str(self.gun)


class Wezipeler(models.Model):
    san=models.IntegerField(default=0)
    Wezipe_at=models.CharField(max_length=50)
    is_bashlayar=models.CharField(default='09:00',max_length=5)
    is_gutaryar=models.CharField(default='17:00',max_length=5)
    obed_bashlayar=models.CharField(default='13:00',max_length=5)
    obed_gutaryar=models.CharField(default='14:00',max_length=5)

    def __str__(self):
        return str(self.Wezipe_at)

    class Meta:
        ordering=['Wezipe_at']

class Rugsatlar(models.Model):
    Rugsat_at=models.CharField(max_length=50)

    def __str__(self):
        return self.Rugsat_at

    class Meta:
        ordering=['Rugsat_at'] 

class Ishgarler(models.Model):
    id=models.AutoField(primary_key=True)
    phone_address=models.CharField(max_length=250,null=True)
    at=models.CharField(max_length=100)
    wezipe=models.ForeignKey(Wezipeler,on_delete=models.CASCADE,related_name='degisli')
    gelen_wagty = JSONField()
    giden_wagty = JSONField()
    is_bashlayar=models.CharField(max_length=5)
    is_gutaryar=models.CharField(max_length=5)
    obed_bashlayar=models.CharField(max_length=5)
    obed_gutaryar=models.CharField(max_length=5)
    barkod_san=models.DecimalField(max_digits=13,decimal_places=0)
    barkod_surat=models.ImageField(upload_to='barcode_img/')
    activesagat=models.IntegerField(default=0)
    activeminut=models.IntegerField(default=0)
    balnoy=models.BooleanField(default=False)
    balnoy_wagt=ArrayField(models.CharField(max_length=10),default=list)
    all_start=ArrayField(models.CharField(max_length=10),default=list)
    all_end=ArrayField(models.CharField(max_length=10),default=list)
    each_start=models.DateField(null=True)
    each_end=models.DateField(null=True)
    balnoy_gornush=models.ForeignKey(Rugsatlar,on_delete=models.CASCADE,default=1)
    balnoy_beyan=models.TextField()
    balnoy_bash=models.DateField(null=True)
    balnoy_sony=models.DateField(null=True)


    def __str__(self):
        return str(self.at)
    
    class Meta:
        ordering=['-id']


    def save(self, *args, **kwargs):
        EAN=barcode.get_barcode_class('Code128')
        ean=EAN(f'{self.barkod_san}',writer=ImageWriter())
        buffer=BytesIO()
        ean.write(buffer, options={"write_text": False})
        self.barkod_surat.save(str(self.at)+'.jpg',File(buffer),save=False)
        return super().save(*args, **kwargs)

class Isgar_Gunler(models.Model):
    day=models.DateField()

    def __str__(self):
        return str(self.day)

    class Meta:
        ordering=['-day']

# +++++++++++++++++++++++++ DIŇLEÝJILER ++++++++++++++++++++++++++++++++++++++++++++++

class Kurslar(models.Model):
    san=models.IntegerField(default=0)
    Kurs_at=models.CharField(max_length=50)
    okuw_bashlayar=models.CharField(max_length=5)
    okuw_gutaryar=models.CharField(max_length=5)

    def __str__(self):
        return str(self.Kurs_at)

    class Meta:
        ordering=['Kurs_at']


class Dinleyjiler(models.Model):
    id=models.AutoField(primary_key=True)
    at=models.CharField(max_length=100)
    kurs=models.ForeignKey(Kurslar,on_delete=models.CASCADE)
    gelen_wagty = JSONField()
    giden_wagty = JSONField()
    okuw_bashlayar=models.CharField(max_length=5)
    okuw_gutaryar=models.CharField(max_length=5)
    barkod_san=models.DecimalField(max_digits=13,decimal_places=0)
    barkod_surat=models.ImageField(upload_to='barcode_img_d/',blank=True)


    def __str__(self):
        return str(self.at)
    
    class Meta:
        ordering=['id']


    def save(self, *args, **kwargs):
        EAN=barcode.get_barcode_class('EAN')
        ean=EAN(f'{self.barkod_san}',writer=ImageWriter())
        buffer=BytesIO()
        ean.write(buffer, options={"write_text": False})
        self.barkod_surat.save(str(self.at)+'.jpg',File(buffer),save=False)
        return super().save(*args, **kwargs)

class Dinleyji_Gunler(models.Model):
    day=models.DateField()

    def __str__(self):
        return str(self.day)

    class Meta:
        ordering=['-day']