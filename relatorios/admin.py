from django.contrib import admin

from relatorios.models import RelatorioPizzaria


class RelatorioPizzariaAdmin(admin.ModelAdmin):
    list_display = ('pizzaria', 'faturamento', 'maior_cliente')
    search_fields = ('pizzaria__nome',)

    def get_queryset(self, request):
        return RelatorioPizzaria.objects.select_related('pizzaria')


admin.site.register(RelatorioPizzaria, RelatorioPizzariaAdmin)
