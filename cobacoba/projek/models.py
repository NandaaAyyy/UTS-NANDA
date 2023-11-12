from django.db import models

class Member(models.Model):
  Nama = models.CharField(max_length=255)
  NPM = models.IntegerField(null=True)
  TANGGAL_LAHIR = models.DateField(null=True)
  UNIVERSITAS = models.CharField(max_length=255)

  def __str__(self):
    return f"{self.Nama}"
  
class Profesi(models.Model):
  Nama = models.CharField(max_length=255)
  Alamat = models.TextField()
  Profesi = models.CharField(max_length=255)


  def __str__(self):
    return f"{self.Nama}"