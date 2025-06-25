import uuid

from rest_framework import serializers

from apps.users_app.models import User


class UserWriteSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'gender', 'birthday', 'password')

    def create(self, validated_data):
       if 'username' not in validated_data:
           validated_data['username'] = f"user_{uuid.uuid4().hex[:10]}"

       user = User.objects.create_user(**validated_data)

       return user

class UserReadSerializer(serializers.ModelSerializer):
    full_age = serializers.ReadOnlyField()

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'gender', 'birthday', 'full_age', 'role')