"""
Tests models for users app.
"""
import pytest
from django.contrib.auth import get_user_model


User = get_user_model()

@pytest.mark.django_db
class TestUserModel:
    def test_create_user_with_required_fields(self):
        user = User.objects.create_user(username="testuser", password="testuser")
        assert user.username == "testuser"
        assert user.check_password("testuser") is True
        assert user.telegram_username is None
        assert user.user_language is None

    def test_create_user_with_optional_fields(self):
        user = User.objects.create_user(
            username="testuser",
            password="testuser",
            telegram_username="test_tg_user",
            first_name="Test",
            last_name="User",
            user_language="en"
        )
        assert user.telegram_username == "test_tg_user"
        assert user.first_name == "Test"
        assert user.last_name == "User"
        assert user.user_language == "en"
