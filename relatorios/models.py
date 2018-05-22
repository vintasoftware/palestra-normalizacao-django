from django.db import models


class RelatorioPizzaria(models.Model):
    pizzaria = models.OneToOneField(
        'pizzarias.Pizzaria', related_name='relatorio', on_delete=models.PROTECT)
    faturamento = models.DecimalField(max_digits=11, decimal_places=2)
    maior_cliente = models.ForeignKey(
        'usuarios.Usuario', null=True, blank=True, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.pizzaria.nome}"
