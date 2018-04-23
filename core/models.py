from django.db import models

# Create your models here.
class noticia(models.Model):
    categoria = models.CharField(max_length=30, default='Geral')
    capa = models.IntegerField(default=0)
    titulo = models.CharField(max_length=300)
    slug = models.SlugField(max_length=300)
    subtitulo = models.CharField(max_length=300, blank=True)
    data = models.DateTimeField(auto_now_add=True)
    autor = models.CharField(max_length=50, default='Redação')
    foto1 = models.CharField(max_length=30, blank=True)
    paragrafo1 = models.TextField(blank=True)
    foto2 = models.CharField(max_length=30, blank=True)
    paragrafo2 = models.TextField(blank=True)

    def __str__(self):
        return self.titulo
