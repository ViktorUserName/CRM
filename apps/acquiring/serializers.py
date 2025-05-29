from rest_framework import serializers

from apps.acquiring.models import AcquiringContract


class ContractReadSerializer(serializers.ModelSerializer):
    client_name = serializers.CharField(source='client.name', read_only=True)
    client_surname = serializers.CharField(source='client.surname', read_only=True)

    class Meta:
        model = AcquiringContract
        fields = ('id', 'client_name','client_surname', 'contract_num', 'acc_num', 'balance', 'commission',
                  'created_at', 'is_active'
        )

class ContractWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = AcquiringContract
        fields = \
                ('contract_num', 'acc_num', 'balance', 'commission',
                'created_at', 'is_active', 'client'
                )

    def create(self, validated_data):
        contract = AcquiringContract.objects.create(**validated_data)

        return contract

    def update(self, instance, validated_data):

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        return instance