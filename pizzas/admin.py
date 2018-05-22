from django.contrib import admin

from pizzas.models import SaborPizza, Ingrediente


class SaborPizzaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'tem_lactose',)
    search_fields = ('nome',)

    def get_queryset(self, request):
        return SaborPizza.objects.annotate_tem_lactose()


admin.site.register(SaborPizza, SaborPizzaAdmin)
admin.site.register(Ingrediente)
