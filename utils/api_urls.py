from rest_framework.routers import DefaultRouter
from django.urls import path, include

from apps.acquiring.views import ContractViewSet, TransactionViewSet
from apps.clients.views import ClientViewSet

router = DefaultRouter()
router.register(r'contracts',   ContractViewSet, basename='contracts')
router.register(r'transactions', TransactionViewSet, basename='transactions')
router.register(r'clients', ClientViewSet, basename='clients')

urlpatterns = [
    path('', include(router.urls)),
]