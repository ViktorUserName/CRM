from rest_framework import viewsets, status
from rest_framework.response import Response

from apps.acquiring.models import AcquiringContract, AcquiringTransactions
from apps.acquiring.serializers import ContractReadSerializer, ContractWriteSerializer, TransactionReadSerializer


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


class TransactionViewSet(viewsets.ModelViewSet):
    queryset = AcquiringTransactions.objects.all()
    serializer_class = TransactionReadSerializer

    # def get_queryset(self):
    #     contract_id = self.kwargs['contract_pk']
    #     return AcquiringTransactions.objects.filter(contract_id=contract_id)

    # def get_serializer_class(self):
    #     if self.action == 'create':
    #         return ContractWriteSerializer
    #     return super().get_serializer_class()