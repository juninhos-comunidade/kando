"""Models do app users.

Define o modelo customizado de User usado para autenticação, que suporta
tanto usuários criados localmente (ex: via createsuperuser) quanto
usuários autenticados através do Supabase Auth.
"""

import uuid

from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.utils import timezone

from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    """Modelo customizado de usuário que autentica via email em vez de username.

    Suporta tanto usuários criados localmente (ex: admin do Django/superusers)
    quanto usuários vinculados a uma conta externa do Supabase Auth através
    do campo `supabase_uid`.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(unique=True)
    full_name = models.CharField(max_length=255)

    # Vincula o registro local a um usuário autenticado via Supabase Auth.
    # Fica nulo para usuários que só existem localmente (ex: criados via createsuperuser).
    supabase_uid = models.UUIDField(unique=True, null=True, blank=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    date_joined = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()

    # Diz ao Django para usar "email" como identificador único de login
    # em vez do campo padrão "username".
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        """Opções de metadata para o modelo User."""
        verbose_name = "user"
        verbose_name_plural = "users"

    def __str__(self):
        """Retorna o email do usuário como representação legível."""
        return self.email
