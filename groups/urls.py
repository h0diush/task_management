from django.urls import path
from rest_framework.routers import DefaultRouter

from groups.views import groups, employees

router = DefaultRouter()

urlpatterns = []

router.register(r'gropus', groups.GroupsView, basename='groups')
router.register(r'(?P<pk>\d+)/employees',
                employees.EmployeesView, basename='employees')
urlpatterns += router.urls
