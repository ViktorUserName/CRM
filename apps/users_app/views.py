from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from apps.users_app.models import User
from apps.users_app.serializers import UserWriteSerializer, UserReadSerializer


class UserRegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserWriteSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        refresh = RefreshToken.for_user(user)
        token_data = {
            'refresh': str(refresh),
            'access': str(refresh.access_token)
        }

        headers = self.get_success_headers(serializer.data)
        return Response(token_data, status=status.HTTP_201_CREATED, headers=headers)


class UserApiInfo(APIView):
    def get(self, request, *args, **kwargs):
        users = User.objects.all()
        serializer = UserReadSerializer(users, many=True)
        return Response(serializer.data)


class ActiveUserView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        serializer = UserReadSerializer(request.user)
        return Response(serializer.data)
