from django.db import models
from django.core.validators import MinValueValidator


class Pedido(models.Model):
    # `on_delete=models.PROTECT` aqui para evitar a deleção de um Endereco
    # relacionado a Pedidos
    endereco_usuario = models.ForeignKey('users.Endereco', on_delete=models.PROTECT)
    # valor_total aqui pois preços dos itens podem mudar:
    valor_total = models.DecimalField(max_digits=6, decimal_places=2)
    data = models.DateTimeField()

    def __str__(self):
        return f"{self.endereco_usuario.usuario.email} - {self.data}"


class ItemPedido(models.Model):
    pedido = models.ForeignKey('Pedido', on_delete=models.CASCADE, related_name='itens')
    # Único jeito de proteger um m2m de deleções é com uma tabela intermediária.
    # Com esta tabela, conseguimos evitar que um Pedido
    # tenha `itens` deletados se tentarem deletar um ItemCardapio.
    # Por isso o `on_delete=models.PROTECT` abaixo:
    item_cardapio = models.ForeignKey('pizzarias.ItemCardapio', on_delete=models.PROTECT)
    # Mas também é necessário esta tabela intermediária porque um ItemPedido tem quantidade:
    quantidade = models.IntegerField(validators=[MinValueValidator(1)])

    def __str__(self):
        return f"({self.pedido}) - ({self.item_cardapio})"
