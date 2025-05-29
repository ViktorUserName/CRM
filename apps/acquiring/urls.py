from rest_framework.routers import DefaultRouter
from django.urls import path, include

from apps.acquiring.views import ContractViewSet, TransactionViewSet

router = DefaultRouter()
router.register(r'contracts', ContractViewSet)
router.register(r'transactions', TransactionViewSet)
urlpatterns = [
    path('', include(router.urls)),
]