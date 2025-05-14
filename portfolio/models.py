from datetime import datetime
from django.db import models

class Programacao(models.Model):
    linguagem = models.CharField(max_length=100, null=False, blank=False)
    legenda = models.CharField(max_length=150, null=False, blank=False)
    imagem = models.ImageField(upload_to="Imagens/%Y/%m/%d/", blank=True)
    publicada = models.BooleanField(default=False)
    data = models.DateTimeField(default=datetime.now, blank=False)

    class Meta:
        verbose_name = "Programação"
        verbose_name_plural = "Programações"
    
    def __str__(self):
        return self.linguagem