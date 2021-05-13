from django.db import models

# Create your models here.
class Localizacao(models.Model):
    rua = models.CharField(max_length=150)
    bairro = models.CharField(max_length=150)
    cidade = models.CharField(max_length=60)
    estado = models.CharField(max_length=2)
    latitude = models.IntegerField(null=True,blank=True)
    longitude = models.IntegerField(null=True,blank=True)

    def __str__(self):
       return self.cidade +"|"+ self.estado
