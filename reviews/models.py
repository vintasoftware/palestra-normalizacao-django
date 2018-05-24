from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class ReviewPizza(models.Model):
    sabor = models.ForeignKey('pizzas.SaborPizza', on_delete=models.CASCADE)
    pizzaria = models.ForeignKey('pizzarias.Pizzaria', on_delete=models.CASCADE)
    avaliacao = models.PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)])

    class Meta:
        unique_together = ('sabor', 'pizzaria')

    def __str__(self):
        return f"{self.sabor.nome} - {self.pizzaria.nome} - {self.avaliacao}"
