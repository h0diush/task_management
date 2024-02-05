from django.urls import path
from rest_framework.routers import DefaultRouter

from works.views import jobs, tasks

router = DefaultRouter()

urlpatterns = []

router.register(r'jobs', jobs.JobViewSet, basename='jobs')
router.register(r'(?P<pk>\d+)/tasks', tasks.TaskView, basename='tasks')

urlpatterns += router.urls
