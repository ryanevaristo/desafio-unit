from django.db import models

# Create your models here.

class Usuario(models.Model):

    STATUS_CHOICES = (
        ("H", "Homologado"),
        ("N", "Não-Homologado"),
    )



    certificado = models.FileField()
    atividade = models.CharField(max_length=200)
    quant_horas = models.CharField('Quantidade de Horas', max_length=20)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, blank=False, null=False)

    def __str__(self):
        return self.atividade