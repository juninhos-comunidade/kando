"""Views do app users.

Define as views de autenticação (login) e as views CRUD para o
modelo User (listar, detalhar, criar, atualizar e remover).
"""

from django.contrib.auth import authenticate
from rest_framework import generics, status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from .models import User
from .serializers import UserSerializer, LoginSerializer


class LoginView(APIView):
    """POST /api/login/ — autentica o usuário e retorna os tokens JWT."""

    permission_classes = [AllowAny]

    def post(self, request):
        """Valida as credenciais e retorna tokens JWT se forem válidas."""
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        email = serializer.validated_data["email"]
        password = serializer.validated_data["password"]

        user = authenticate(request, email=email, password=password)

        if user is None:
            return Response(
                {"detail": "Credenciais inválidas."},
                status=status.HTTP_401_UNAUTHORIZED,
            )

        refresh = RefreshToken.for_user(user)

        return Response(
            {
                "access": str(refresh.access_token),
                "refresh": str(refresh),
                "user_id": str(user.id),
                "email": user.email,
            },
            status=status.HTTP_200_OK,
        )


class UserListView(generics.ListAPIView):
    """GET /api/users/ — lista todos os usuários."""

    queryset = User.objects.all().order_by("-date_joined")
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated] 
"""
Durante o desenvolvimento permission_classes sera 'isAuthenticated', 
mas sera alterado para 'IsAdmin' conforme o projeto avance
"""

class UserDetailView(generics.RetrieveAPIView):
    """GET /api/users/<pk>/ — detalhe de um usuário."""

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
"""
Durante o desenvolvimento permission_classes sera 'isAuthenticated', 
mas sera alterado para 'IsAdmin' conforme o projeto avance
"""

class UserCreateView(generics.CreateAPIView):
    """POST /api/users/create/ — cadastro público de usuário."""

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]


class UserUpdateView(generics.UpdateAPIView):
    """PUT/PATCH /api/users/<pk>/update/ — atualização de usuário."""

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
"""
Durante o desenvolvimento permission_classes sera 'isAuthenticated', 
mas sera alterado para 'IsAdmin' conforme o projeto avance
"""

class UserDeleteView(generics.DestroyAPIView):
    """DELETE /api/users/<pk>/delete/ — remoção de usuário."""

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
"""
Durante o desenvolvimento permission_classes sera 'isAuthenticated', 
mas sera alterado para 'IsAdmin' conforme o projeto avance
"""