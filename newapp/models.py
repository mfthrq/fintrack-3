from django.db import models

class Income(models.Model):
    tanggal = models.DateField()
    jumlah = models.DecimalField(max_digits=100, decimal_places=0)
    sumber = models.CharField(max_length=255)
    deskripsi = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.tanggal} - {self.sumber} - Rp{self.jumlah}"
    
class Outcome(models.Model):
    tanggal = models.DateField()
    jumlah = models.DecimalField(max_digits=100, decimal_places=0)
    sumber = models.CharField(max_length=255)
    deskripsi = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.tanggal} - {self.sumber} - Rp{self.jumlah}"