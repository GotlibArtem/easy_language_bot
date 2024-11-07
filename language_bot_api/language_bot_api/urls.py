"""
URL Configuration for language_bot_api project.
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions


api_urls = [
    path('users/', include('users.urls')),
]

schema_view = get_schema_view(
    openapi.Info(
        title="Personal Language Bot API",
        default_version='v1',
        description="API телеграм-бота Personal Language Bot",
    ),
    patterns=[path('api/', include(api_urls)), ],
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('api-ui/',
         TemplateView.as_view(template_name='swaggerui/swaggerui.html',
                              extra_context={'schema_url': 'openapi-schema'}),
         name='swagger-ui'),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$',
            schema_view.without_ui(cache_timeout=0),
            name='schema-json'),
    path('admin/', admin.site.urls),
    path('api/', include(api_urls)),
]
