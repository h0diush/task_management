from django.contrib.auth import get_user_model
from drf_spectacular.utils import extend_schema_view, extend_schema
from rest_framework import generics, status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from users.serializers.api import users as users_s

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


@extend_schema_view(
    get=extend_schema(summary="Профиль пользователя",
                      tags=["Пользователи"]),
    put=extend_schema(summary="Изменить профиль пользователя",
                      tags=["Пользователи"]),
    patch=extend_schema(summary="Изменить частично профиль пользователя",
                        tags=["Пользователи"]),
)
class MeView(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]
    http_method_names = ["get", "patch"]

    def get_object(self):
        return self.request.user

    def get_serializer_class(self):
        if self.request.method in ['PUT', 'PATCH']:
            return users_s.UserUpdateSerializer
        return users_s.MeListSerializer


@extend_schema_view(
    post=extend_schema(request=users_s.ChangePasswordSerializer,
                       summary="Смена пароля",
                       tags=["Аутентификация и Регистрация"])
)
class ChangePasswordView(APIView):

    def post(self, request):
        user = request.user
        serializer = users_s.ChangePasswordSerializer(
            instance=user, data=request.data
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
