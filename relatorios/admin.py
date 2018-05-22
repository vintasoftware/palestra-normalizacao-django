from django.contrib import admin

from relatorios.models import RelatorioPizzaria


class RelatorioPizzariaAdmin(admin.ModelAdmin):
    list_display = ('pizzaria', 'faturamento', 'maior_cliente')
    search_fields = ('pizzaria__nome',)


admin.site.register(RelatorioPizzaria, RelatorioPizzariaAdmin)
