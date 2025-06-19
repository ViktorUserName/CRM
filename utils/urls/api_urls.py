from django.urls import path, include

from apps.acquiring.views import ContractViewSet, TransactionViewSet
from apps.clients.views import ClientViewSet
from utils.router import CustomRouter

from apps.users_app.views import UserRegisterView, UserApiInfo, ActiveUserView

router = CustomRouter(custom_routes={
    'sign-in': 'sign-in',
    'active-user': 'active-user',
    # 'users': 'users'
})


router.register(r'contracts',   ContractViewSet, basename='contracts')
router.register(r'transactions', TransactionViewSet, basename='transactions')
router.register(r'clients', ClientViewSet, basename='clients')


urlpatterns = [
    path('', include(router.urls)),
    path(r'sign-in', UserRegisterView.as_view(), name='sign-in'),
    # path(r'users/', UserApiInfo.as_view(), name='users'),
    path(r'active-user/', ActiveUserView.as_view(), name='active-user'),
]