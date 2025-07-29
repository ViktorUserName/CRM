from rest_framework import serializers

from apps.credit.models import RequestCredit, CreditContract, CreditBalance, CreditTransaction


class RequestCreditSerializer(serializers.ModelSerializer):
    class Meta:
        model = RequestCredit
        fields = '__all__'


class CreditContractSerializer(serializers.ModelSerializer):
    class Meta:
        model = CreditContract
        fields = '__all__'


class CreditBalanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = CreditBalance
        fields = '__all__'


class CreditTransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CreditTransaction
        fields = '__all__'