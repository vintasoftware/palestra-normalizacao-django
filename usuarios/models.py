from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils.translation import ugettext_lazy as _

from .managers import UsuarioManager


class Usuario(AbstractBaseUser, PermissionsMixin, models.Model):
    email = models.EmailField(max_length=255, unique=True)
    is_staff = models.BooleanField(
        default=False,
        help_text=_('Designates whether the user can log into this admin '
                    'site.'))
    is_active = models.BooleanField(
        default=True,
        help_text=_('Designates whether this user should be treated as '
                    'active. Unselect this instead of deleting accounts.'))

    objects = UsuarioManager()

    USERNAME_FIELD = 'email'

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email

    def __str__(self):
        return self.email


class Endereco(models.Model):
    usuario = models.ForeignKey(
        'usuarios.Usuario', related_name='enderecos', on_delete=models.CASCADE)
    endereco = models.TextField()
    ativo = models.BooleanField()

    def __str__(self):
        return f"{self.usuario.email} - {self.endereco}"
