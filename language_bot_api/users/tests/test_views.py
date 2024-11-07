"""
Tests views for users app.
"""
import pytest
from django.urls import reverse
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.test import APIClient


User = get_user_model()

@pytest.mark.django_db
class TestUserCreateView:
    def setup_method(self):
        self.client = APIClient()
        self.url = reverse('create_user')

    def test_create_user_success(self):
        data = {
            "username": "apiuser",
            "telegram_username": "api_tg_user",
            "first_name": "Test",
            "last_name": "User",
            "user_language": "en"
        }
        response = self.client.post(self.url, data, format='json')

        assert response.status_code == status.HTTP_201_CREATED
        user_exists = User.objects.filter(username="apiuser").exists()
        assert user_exists is True

    def test_create_user_already_exists(self):
        User.objects.create_user(username="existing_api_user", password="password123")
        data = {
            "username": "existing_api_user",
            "telegram_username": "existing_tg_user",
            "first_name": "Existing",
            "last_name": "User",
            "user_language": "en"
        }

        response = self.client.post(self.url, data, format='json')

        assert response.status_code == status.HTTP_400_BAD_REQUEST
