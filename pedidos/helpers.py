
def calcular_valor_total_pedido(pedido):
    # Este cálculo é feito a nível de Python mesmo
    # pois `Pedido.valor_total` é uma coluna histórica
    return sum(
        item_pedido.item_cardapio.preco * item_pedido.quantidade
        for item_pedido in pedido.itens.all())
