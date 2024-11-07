"""
Serializsers for users app.
"""
from django.contrib.auth import get_user_model
from rest_framework import serializers


User = get_user_model()

class UserCreateSerializer(serializers.ModelSerializer):
    telegram_username = serializers.CharField(required=False, allow_blank=True)
    first_name = serializers.CharField(required=False, allow_blank=True)
    last_name = serializers.CharField(required=False, allow_blank=True)
    user_language = serializers.CharField(required=False, allow_blank=True)

    class Meta:
        model = User
        fields = ['username', 'telegram_username', 'first_name', 'last_name', 'user_language']

    def create(self, validated_data):
        """Method create"""
        username = validated_data.get('username')
        if User.objects.filter(username=username).exists():
            raise serializers.ValidationError("A user with this username already exists.")
        user = User.objects.create_user(
            username=username,
            password=username,  # The default password is username
            telegram_username=validated_data.get('telegram_username', ""),
            first_name=validated_data.get('first_name', ""),
            last_name=validated_data.get('last_name', ""),
            user_language=validated_data.get('user_language', "")
        )
        return user
