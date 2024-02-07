from django.urls import path

from users.views.users import RegistrationView, MeView, ChangePasswordView

urlpatterns = [
    path('users/reg/', RegistrationView.as_view(), name='reg'),
    path('users/me/', MeView.as_view(), name='me'),
    path('users/change_password/', ChangePasswordView.as_view(),
         name='change-password'),
]
