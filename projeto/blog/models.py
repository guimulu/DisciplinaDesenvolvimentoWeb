from django.db import models
from django.utils import timezone
# Create your models here.
class Post(models.Model):
    titulo = models.CharField(max_length=200)
    texto = models.TextField()
    data_criacao = models.DateTimeField(default=timezone.now)
    data_publicacao = models.DateTimeField(null = True, blank = True)
    autor = models.ForeignKey("auth.User")

    def __str__(self):
        return str(self.titulo.encode("utf-8"))


class Comentario(models.Model):
    texto = models.TextField()
    data_publicacao = models.DateTimeField(default=timezone.now())
    autor = models.ForeignKey('auth.User')
    post = models.ForeignKey('Post')