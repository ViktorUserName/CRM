from rest_framework import serializers

from apps.clients.models.models import Client, LegalDetails, IndividualDetails


class LegalDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = LegalDetails
        fields = ['inn', 'kpp', 'ogrn', 'address']


class IndividualDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = IndividualDetails
        fields = ['passport_number', 'birth_date', 'unp']


class ClientReadSerializer(serializers.ModelSerializer):
    legal_details = LegalDetailsSerializer(source='legaldetails', required=False)
    individual_details = IndividualDetailsSerializer(source='individualdetails', required=False)

    class Meta:
        model = Client
        fields = ['id', 'name', 'surname', 'email', 'phone', 'is_legal', 'legal_details', 'individual_details']

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #
    #     is_legal = None
    #
    #     if self.instance:
    #         is_legal = getattr(self.instance, 'is_legal', None)
    #
    #     if is_legal:
    #         self.fields.pop('individual_details', None)
    #     else:
    #         self.fields.pop('legal_details', None)


class ClientCreateSerializer(serializers.ModelSerializer):
    legal_details = LegalDetailsSerializer(required=False)
    individual_details = IndividualDetailsSerializer(required=False)

    class Meta:
        model = Client
        fields = ['name', 'surname', 'email', 'phone', 'is_legal', 'legal_details', 'individual_details']

    def create(self, validated_data):
        legal_data = validated_data.pop('legal_details', None)
        individual_data = validated_data.pop('individual_details', None)

        client = Client.objects.create(**validated_data)

        if client.is_legal and legal_data:
            LegalDetails.objects.create(client=client, **legal_data)
        elif not client.is_legal and individual_data:
            IndividualDetails.objects.create(client=client, **individual_data)

        return client

    def update(self, instance, validated_data):
        legal_data = validated_data.pop('legal_details', None)
        individual_data = validated_data.pop('individual_details', None)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        if instance.is_legal and legal_data:
            legal_details_obj, created = LegalDetails.objects.get_or_create(client=instance)
            for attr, value in legal_data.items():
                setattr(legal_details_obj, attr, value)
            legal_details_obj.save()

        elif not instance.is_legal and individual_data:
            individual_details_obj, created = IndividualDetails.objects.get_or_create(client=instance)
            for attr, value in individual_data.items():
                setattr(individual_details_obj, attr, value)
            individual_details_obj.save()

        return instance
