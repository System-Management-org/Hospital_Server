from django.contrib.auth.models import User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')

        # Ensure the password is write-only and not included in responses
        extra_kwargs = {'password': {'write_only': True}}

    # Override create method to properly hash the password
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user