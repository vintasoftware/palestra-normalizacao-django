from django.contrib import admin

from pedidos.models import ItemPedido, Pedido
from pedidos.helpers import calcular_valor_total_pedido


class ItemPedidoInline(admin.StackedInline):
    model = ItemPedido


class PedidoAdmin(admin.ModelAdmin):
    search_fields = ('endereco_usuario__usuario__email',)
    inlines = (ItemPedidoInline,)
    readonly_fields = ('valor_total',)

    def save_model(self, request, obj, form, change):
        obj.valor_total = 0

        super().save_model(request, obj, form, change)

    def save_related(self, request, form, formsets, change):
        super().save_related(request, form, formsets, change)

        form.instance.valor_total = calcular_valor_total_pedido(form.instance)
        form.instance.save()


admin.site.register(Pedido, PedidoAdmin)
admin.site.register(ItemPedido)
