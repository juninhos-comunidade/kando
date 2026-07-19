"""Managers do app users.

Define o manager customizado usado pelo modelo User, responsável por
criar usuários e superusers corretamente (já que o User usa email
em vez de username).
"""

from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):
    """Manager customizado para o modelo User baseado em email.

    Sobrescreve a criação de usuários para usar email como identificador
    e lidar corretamente com senha opcional (usuários vindos do Supabase
    podem não ter senha local).
    """

    use_in_migrations = True

    def _create_user(self, email, password=None, **extra_fields):
        """Cria e salva um usuário com o email e senha informados.

        Método interno usado por `create_user` e `create_superuser`.
        Se nenhuma senha for passada, o usuário é criado com senha
        inutilizável (ex: autenticação feita via Supabase).
        """
        if not email:
            raise ValueError("O email é obrigatório.")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        if password:
            user.set_password(password)
        else:
            user.set_unusable_password()
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        """Cria um usuário comum (não staff, não superuser) por padrão."""
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        """Cria um superuser, validando as flags e senha obrigatórias."""
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser precisa ter is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser precisa ter is_superuser=True.")
        if not password:
            raise ValueError("Superuser precisa de uma senha.")

        return self._create_user(email, password, **extra_fields)
    