from django.db import models


class Pizzaria(models.Model):
    nome = models.CharField(max_length=255)

    def __str__(self):
        return self.nome
