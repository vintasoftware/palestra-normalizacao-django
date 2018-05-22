from django.db import models


class Pizzaria(models.Model):
    nome = models.CharField(max_length=255)

    def __str__(self):
        return self.nome


class ItemCardapio(models.Model):
    pizzaria = models.ForeignKey('pizzarias.Pizzaria', on_delete=models.PROTECT)
    sabor = models.ForeignKey('pizzas.SaborPizza', on_delete=models.PROTECT)
    preco = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.pizzaria.nome} - {self.sabor.nome} - {self.preco}"
