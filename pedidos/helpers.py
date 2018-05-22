
def calcular_valor_total_pedido(pedido):
    return sum(
        item_pedido.item_cardapio.preco * item_pedido.quantidade
        for item_pedido in pedido.itens.all())
