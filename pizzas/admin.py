from django.contrib import admin

from pizzas.models import SaborPizza, Ingrediente


class TemLactoseListFilter(admin.SimpleListFilter):
    title = "Tem Lactose"
    parameter_name = '_tem_lactose'

    def lookups(self, request, model_admin):
        return (
            ('1', "True"),
            ('0', "False"),
        )

    def queryset(self, request, queryset):
        if self.value() == '1':
            return queryset.com_lactose()
        elif self.value() == '0':
            return queryset.sem_lactose()


class SaborPizzaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'tem_lactose',)
    search_fields = ('nome',)
    list_filter = (TemLactoseListFilter,)

    def get_queryset(self, request):
        return SaborPizza.objects.annotate_tem_lactose()


admin.site.register(SaborPizza, SaborPizzaAdmin)
admin.site.register(Ingrediente)
