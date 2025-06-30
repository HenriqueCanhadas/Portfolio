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


class Modulo(models.Model):
    programacao = models.ForeignKey(
        Programacao,
        related_name='modulos',
        on_delete=models.CASCADE
    )
    titulo = models.CharField(max_length=200)
    link = models.URLField(max_length=500)

    class Meta:
        verbose_name = "Módulo"
        verbose_name_plural = "Módulos"
    
    def __str__(self):
        return self.titulo
