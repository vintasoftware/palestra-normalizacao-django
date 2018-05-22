from relatorios.models import RelatorioPizzaria
from pizzarias.models import Pizzaria
from usuarios.models import Usuario


def atualizar_relatorios_pizzaria():
    todas_pizzarias = list(
        Pizzaria.objects.all()
        .annotate_faturamento()
        .annotate_maior_cliente_id())

    # prefetch Usuarios maior_cliente_id manualmente
    maiores_clientes = Usuario.objects.filter(id__in=[p.maior_cliente_id for p in todas_pizzarias])
    id_maiores_clients_dict = {c.id: c for c in maiores_clientes}

    for pizzaria in todas_pizzarias:
        RelatorioPizzaria.objects.update_or_create(
            pizzaria=pizzaria,
            defaults={
                'faturamento': pizzaria.faturamento or 0,
                'maior_cliente': id_maiores_clients_dict.get(pizzaria.maior_cliente_id)
            })
