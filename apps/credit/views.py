from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from apps.credit.models import RequestCredit
from apps.credit.serializers import RequestCreditSerializer


class RequestCreditViewSet(viewsets.ModelViewSet):
    queryset = RequestCredit.objects.all()
    serializer_class = RequestCreditSerializer

    def get_permissions(self):
        self.permission_classes = [IsAuthenticated]
