from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import ugettext_lazy as _

from usuarios.models import Usuario, Endereco


class UsuarioAdmin(UserAdmin):
    list_display = ('id', 'email',)
    list_filter = ('is_active', 'is_staff', 'groups',)
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ('groups', 'user_permissions',)

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')}),
    )


admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Endereco)
