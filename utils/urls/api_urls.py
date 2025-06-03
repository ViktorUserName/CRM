from django.urls import path, include

from apps.acquiring.views import ContractViewSet, TransactionViewSet
from apps.clients.views import ClientViewSet
from utils.router import CustomRouter

from apps.users_app.views import UserRegisterView, UserApiInfo


router = CustomRouter(custom_routes={
    'sign-in': 'sign-in',
    'users': 'users'
})


router.register(r'contracts',   ContractViewSet, basename='contracts')
router.register(r'transactions', TransactionViewSet, basename='transactions')
router.register(r'clients', ClientViewSet, basename='clients')


urlpatterns = [
    path('', include(router.urls)),
    path(r'sign-in', UserRegisterView.as_view(), name='sign-in'),
    path(r'users/', UserApiInfo.as_view(), name='users'),
]