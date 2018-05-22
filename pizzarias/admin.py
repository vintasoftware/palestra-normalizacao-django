from django.contrib import admin

from pizzarias.models import ItemCardapio, Pizzaria


class ItemCardapioInline(admin.StackedInline):
    model = ItemCardapio


class PizzariaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'faturamento', 'maior_cliente_id')
    search_fields = ('nome',)
    inlines = (ItemCardapioInline,)

    def get_queryset(self, request):
        return Pizzaria.objects.annotate_faturamento().annotate_maior_cliente_id()


admin.site.register(Pizzaria, PizzariaAdmin)
admin.site.register(ItemCardapio)
