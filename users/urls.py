from django.urls import path, include
# from rest_framework.routers import DefaultRouter
from users.views.users import RegistrationView

# router = DefaultRouter()

urlpatterns = [
    path('users/reg/', RegistrationView.as_view(), name='reg'),
]

# urlpatterns += router.urls
