from django.urls import path, include

from api.spectacular.urls import urlpatterns as doc_urls
from groups.urls import urlpatterns as group_urls
from users.urls import urlpatterns as user_urls

app_name = 'api'

urlpatterns = [
    path('auth/', include('djoser.urls.jwt')),
]

urlpatterns += doc_urls
urlpatterns += user_urls
urlpatterns += group_urls
