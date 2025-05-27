from rest_framework import viewsets, status
from rest_framework.response import Response

from apps.clients.models.models import Client
from apps.clients.serializers import ClientCreateSerializer, ClientReadSerializer


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientReadSerializer

    def get_serializer_class(self):
        if self.action == 'create':
            return ClientCreateSerializer
        return super().get_serializer_class()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)  # <-- обязательно data=
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


