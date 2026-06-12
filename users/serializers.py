from rest_framework import serializers

from users.models import CustomUser


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ("email", "username", "password")

    def create(self, validated_data):
        return CustomUser.objects.create_user(**validated_data)
