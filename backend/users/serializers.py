"""Serializers do app users.

Define os serializers usados pelas rotas de autenticação e cadastro
de usuários.
"""

from rest_framework import serializers

from .models import User


class UserSerializer(serializers.ModelSerializer):
    """Serializer único usado por todas as rotas de users.

    is_superuser não entra nos fields de propósito: superuser só é criado via
    `createsuperuser` ou admin do Django. is_staff é somente leitura pelo mesmo
    motivo - esse serializer também atende o cadastro público (create com
    AllowAny), então nenhum campo de privilégio pode ser gravável aqui.
    """

    password = serializers.CharField(write_only=True, required=False, allow_blank=False)

    class Meta:
        """Configuração do serializer: modelo e campos expostos."""

        model = User
        fields = [
            "id",
            "email",
            "full_name",
            "supabase_uid",
            "is_active",
            "is_staff",
            "date_joined",
            "updated_at",
            "password",
        ]
        read_only_fields = ["id", "is_staff", "date_joined", "updated_at"]

    def create(self, validated_data):
        """Cria um novo usuário, definindo senha (ou deixando inutilizável)."""
        password = validated_data.pop("password", None)
        user = User(**validated_data)
        if password:
            user.set_password(password)
        else:
            user.set_unusable_password()
        user.save()
        return user

    def update(self, instance, validated_data):
        """Atualiza um usuário existente, trocando a senha se informada."""
        password = validated_data.pop("password", None)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        if password:
            instance.set_password(password)
        instance.save()
        return instance


class LoginSerializer(serializers.Serializer):
    """Serializer usado apenas para validar as credenciais de login."""

    email = serializers.EmailField()
    password = serializers.CharField(write_only=True, trim_whitespace=False)
