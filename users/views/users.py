from django.contrib.auth import get_user_model
from drf_spectacular.utils import extend_schema_view, extend_schema
from rest_framework import generics
from users.serializers.api import users as users_s
from rest_framework.permissions import AllowAny
User = get_user_model()


@extend_schema_view(
    post=extend_schema(
        summary="Регистрация пользователя",
        tags=["Аутентификация и Регистрация"]
    )
)
class RegistrationView(generics.CreateAPIView):
    serializer_class = users_s.RegisterSerializer
    permission_classes = [AllowAny]
    queryset = User.objects.all()

    
