from django.db import models
from django.db.models import JSONField


class Toparlar(models.Model):
    Topar_at=models.CharField(max_length=50)

    def __str__(self):
        return str(self.Topar_at)

    class Meta:
        ordering=['Topar_at']


class DeviceId(models.Model):
    username = models.CharField(max_length=100)
    device_id = models.CharField(max_length=10485760, unique=True)

    def __str__(self):
        return self.device_id

class Talyplar(models.Model):
    at=models.CharField(max_length=100)
    device_id = models.OneToOneField(DeviceId, on_delete=models.CASCADE, null=True)
    topar=models.ForeignKey(Toparlar,on_delete=models.CASCADE,related_name='degisli')
    gelen_wagty = JSONField()
    ID_NO=models.IntegerField()

    def __str__(self):
        return str(self.at)
    
    class Meta:
        ordering=['at']


class Talyp_Gunler(models.Model):
    day=models.DateField()

    def __str__(self):
        return str(self.day)

    class Meta:
        ordering=['-day']