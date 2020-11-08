"""emenu URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import obtain_auth_token

import api.views as emenu
from .api import router


schema_view = get_schema_view(
    openapi.Info(
        title="e-menu API",
        default_version="v1",
        description="This is auto-generated documentation for example restaurant's API",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

decorated_auth_view = swagger_auto_schema(
    method="post", request_body=AuthTokenSerializer
)(obtain_auth_token)

urlpatterns = [
    path("admin", admin.site.urls),
    path("auth", decorated_auth_view, name="token_auth"),
    path(
        "invalidate",
        emenu.authorization.InvalidateToken.as_view(),
        name="invalidate_token",
    ),
    path(
        "menu/<int:id>/details",
        emenu.menu_details.MenuDetailsView.as_view(),
        name="get_menu_details",
    ),
    path("menus/", include((router.urls, "emenu"), namespace="menus")),
    path(
        r"swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
]
