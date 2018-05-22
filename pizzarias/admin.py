from django.contrib import admin

from pizzarias.models import ItemCardapio, Pizzaria


class ItemCardapioInline(admin.StackedInline):
    model = ItemCardapio


class PizzariaAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)
    inlines = (ItemCardapioInline,)


admin.site.register(Pizzaria, PizzariaAdmin)
admin.site.register(ItemCardapio)
