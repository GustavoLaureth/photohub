from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError

class Tag(models.Model):
    nome = models.CharField(max_length=255)

    def __str__(self):
        return self.nome

class Cliente(models.Model):
    imagem = models.ImageField(upload_to='imagens/', max_length=500, default='0', blank=True)
    titulo = models.CharField(max_length=255)
    descricao = models.TextField(blank=True)
    tags = models.ManyToManyField(Tag)
    data_criacao = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.titulo
    
    def clean(self):
        if self.pk:
            if self.tags.count() > 3:
                raise ValidationError("O cliente deve ter exatamente 3 tags.")

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.clean()

    def delete(self, *args, **kwargs):
        self.imagem.delete()
        super().delete(*args, **kwargs)