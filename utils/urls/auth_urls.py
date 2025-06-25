from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from apps.users_app.views import UserRegisterView, UserApiInfo
from utils.router import CustomRouter


router = CustomRouter(custom_routes={
    # 'users': 'users',

    'sign-up': 'sign-up',
    'sign-in': 'sign-in',
    'refresh': 'refresh'
})


urlpatterns = [
    path('', include(router.urls)),
    # path(r'users/', UserApiInfo.as_view(), name='users'),

    path(r'sign-up/', UserRegisterView.as_view(), name='sign-up'),
    path('sign-in/', TokenObtainPairView.as_view(), name='sign-in'),
    path('refresh/', TokenRefreshView.as_view(), name='refresh'),

]