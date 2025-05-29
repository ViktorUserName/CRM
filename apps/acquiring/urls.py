from rest_framework.routers import DefaultRouter
from django.urls import path, include

from apps.acquiring.views import ContractViewSet

router = DefaultRouter()
router.register(r'', ContractViewSet)
urlpatterns = [
    path('', include(router.urls)),
]