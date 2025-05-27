from rest_framework.routers import DefaultRouter
from django.urls import path, include

from apps.clients.views import ClientViewSet

router = DefaultRouter()
router.register(r'', ClientViewSet)
urlpatterns = [
    path('', include(router.urls)),
]