from django.contrib import admin
from django.urls import include, path, re_path
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Registration Service API",
        default_version='v1',
        description="API para registro de alunos",
    ),
    public=True,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^v1/docs/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^v1/api/', include('apps.registration.urls')),
]
