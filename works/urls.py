from django.urls import path
from rest_framework.routers import DefaultRouter

from works.views import jobs
router = DefaultRouter()

urlpatterns = []

router.register(r'jobs', jobs.JobViewSet, basename='jobs')

urlpatterns += router.urls
