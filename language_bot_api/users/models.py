"""
Models description for users app.
"""
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class CustomUser(AbstractUser):
    """Custom user's model"""
    telegram_username = models.CharField(
        max_length=150,
        blank=True, null=True,
        verbose_name=_("Telegram username"),
    )
    user_language = models.CharField(
        max_length=10,
        blank=True, null=True,
        verbose_name=_("User language code"),
    )

    def __str__(self):
        return f'ID: {self.username}, username: {self.telegram_username}'
