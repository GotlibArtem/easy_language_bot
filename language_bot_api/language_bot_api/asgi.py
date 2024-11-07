"""
ASGI config for language_bot_api project.
"""
import os

from django.core.asgi import get_asgi_application


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'language_bot_api.settings')

application = get_asgi_application()
