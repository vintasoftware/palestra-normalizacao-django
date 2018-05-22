from django.db import models
from django.core.validators import MinValueValidator
from django.core.exceptions import ValidationError


class Pedido(models.Model):
    pizzaria = models.ForeignKey(
        'pizzarias.Pizzaria', related_name='pedidos', on_delete=models.CASCADE)
    # `on_delete=models.PROTECT` aqui para evitar a deleção de um Endereco
    # relacionado a Pedidos
    endereco_usuario = models.ForeignKey(
        'usuarios.Endereco', related_name='pedidos', on_delete=models.PROTECT)
    # valor_total aqui pois preços dos itens podem mudar:
    valor_total = models.DecimalField(max_digits=6, decimal_places=2)
    data = models.DateTimeField()

    def __str__(self):
        return f"{self.endereco_usuario.usuario.email} - {self.data}"


class ItemPedido(models.Model):
    pedido = models.ForeignKey('pedidos.Pedido', related_name='itens', on_delete=models.CASCADE)
    # Único jeito de proteger um m2m de deleções é com uma tabela intermediária.
    # Com esta tabela, conseguimos evitar que um Pedido
    # tenha `itens` deletados se tentarem deletar um ItemCardapio.
    # Por isso o `on_delete=models.PROTECT` abaixo:
    item_cardapio = models.ForeignKey('pizzarias.ItemCardapio', on_delete=models.PROTECT)
    # Mas também é necessário esta tabela intermediária porque um ItemPedido tem quantidade:
    quantidade = models.IntegerField(validators=[MinValueValidator(1)])

    def clean(self):
        if not self.pedido.pizzaria.itens_cardapio.filter(id=self.item_cardapio.id).exists():
            raise ValidationError(
                f"O item \"{self.item_cardapio}\" não pertence "
                f"a Pizzaria \"{self.pedido.pizzaria}\"")

    def __str__(self):
        return f"({self.pedido}) - ({self.item_cardapio})"
