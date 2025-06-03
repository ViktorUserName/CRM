from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

from apps.users_app.views import UserApiInfo
from utils.router import CustomRouter

router = CustomRouter(custom_routes={
    # 'sign-in': 'sign-in',
    # 'users' : 'users'
})

router.register('api', include(router.urls))



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    # path('v1/', include('utils.urls.api_urls')),

    path('auth/sign-in/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('silk/', include('silk.urls', namespace='silk')),
    path('schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]