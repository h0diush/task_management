from django.urls import path
from rest_framework.routers import DefaultRouter

from groups.views import groups

router = DefaultRouter()

urlpatterns = []

router.register(r'gropus', groups.GroupsView, basename='groups')

urlpatterns += router.urls
