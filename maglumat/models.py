from django.db import models
from django.db.models import JSONField
import barcode
from barcode.writer import ImageWriter
from io import BytesIO
from django.core.files import File

class del_info_gun(models.Model):
    gun=models.CharField(max_length=10)

    def __str__(self):
        return str(self.gun)


class Toparlar(models.Model):
    Topar_at=models.CharField(max_length=50)

    def __str__(self):
        return str(self.Topar_at)

    class Meta:
        ordering=['Topar_at']


class Talyplar(models.Model):
    at=models.CharField(max_length=100)
    topar=models.ForeignKey(Toparlar,on_delete=models.CASCADE,related_name='degisli')
    gelen_wagty = JSONField()
    ID_NO=models.IntegerField()
    barkod_san=models.DecimalField(max_digits=13,decimal_places=0)
    barkod_surat=models.ImageField(upload_to='barcode_img/')

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

class Talyp_Gunler(models.Model):
    day=models.DateField()

    def __str__(self):
        return str(self.day)

    class Meta:
        ordering=['-day']