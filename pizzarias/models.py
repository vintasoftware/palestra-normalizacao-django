from django.db import models
from django.db.models import Sum, OuterRef, Subquery

from usuarios.models import Usuario


class PizzariaQuerySet(models.QuerySet):

    def annotate_faturamento(self):
        return self.annotate(_faturamento=Sum('pedidos__valor_total'))

    def annotate_maior_cliente_id(self):
        maior_cliente_id_subquery = Usuario.objects.filter(
            enderecos__pedidos__pizzaria=OuterRef('pk'),
        ).annotate(
            _valor_total_pedidos=Sum('enderecos__pedidos__valor_total')
        ).order_by(
            '-_valor_total_pedidos'
        ).values('id')[:1]
        return self.annotate(_maior_cliente_id=Subquery(maior_cliente_id_subquery))


class Pizzaria(models.Model):
    nome = models.CharField(max_length=255)

    objects = PizzariaQuerySet.as_manager()

    def __str__(self):
        return self.nome

    @property
    def faturamento(self):
        if hasattr(self, '_faturamento'):
            return self._faturamento

        return Pizzaria.objects.filter(pk=self.pk)\
            .annotate_faturamento().values('_faturamento').get()['_faturamento']

    @property
    def maior_cliente_id(self):
        if hasattr(self, '_maior_cliente_id'):
            return self._maior_cliente_id

        return Pizzaria.objects.filter(pk=self.pk)\
            .annotate_maior_cliente_id().values('_maior_cliente_id').get()['_maior_cliente_id']


class ItemCardapio(models.Model):
    pizzaria = models.ForeignKey(
        'pizzarias.Pizzaria', related_name='itens_cardapio', on_delete=models.PROTECT)
    sabor = models.ForeignKey('pizzas.SaborPizza', on_delete=models.PROTECT)
    preco = models.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        unique_together = ('pizzaria', 'sabor')

    def __str__(self):
        return f"{self.pizzaria.nome} - {self.sabor.nome} - {self.preco}"
