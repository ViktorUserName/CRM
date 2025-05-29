from rest_framework import viewsets, status
from rest_framework.response import Response

from apps.acquiring.models import AcquiringContract
from apps.acquiring.serializers import ContractReadSerializer, ContractWriteSerializer


class ContractViewSet(viewsets.ModelViewSet):
    queryset = AcquiringContract.objects.all()
    serializer_class = ContractReadSerializer

    def get_serializer_class(self):
        if self.action == 'create':
            return ContractWriteSerializer
        return super().get_serializer_class()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)