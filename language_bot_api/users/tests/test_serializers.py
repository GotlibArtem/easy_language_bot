"""
Tests serializers for users app.
"""
import pytest
from django.contrib.auth import get_user_model
from users.serializers import UserCreateSerializer


User = get_user_model()

@pytest.mark.django_db
class TestUserCreateSerializer:
    def test_serializer_valid_data(self):
        data = {
            "username": "newuser",
            "telegram_username": "new_tg_user",
            "first_name": "New",
            "last_name": "User",
            "user_language": "en"
        }

        serializer = UserCreateSerializer(data=data)
        assert serializer.is_valid() is True
        user = serializer.save()

        assert user.username == "newuser"
        assert user.telegram_username == "new_tg_user"
        assert user.first_name == "New"
        assert user.last_name == "User"
        assert user.user_language == "en"

    def test_serializer_existing_user(self):
        User.objects.create_user(username="existinguser", password="existinguser")
        data = {"username": "existinguser"}
        serializer = UserCreateSerializer(data=data)
        assert serializer.is_valid() is False
