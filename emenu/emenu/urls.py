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
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from .api import router
import api.views as emenu


urlpatterns = [
    path("admin", admin.site.urls),
    path("auth", obtain_auth_token, name="token_auth"),
    path("invalidate", emenu.authorization.InvalidateToken.as_view(), name="invalidate_token"),
    path("menus_old", emenu.public_views.MenusListView.as_view(), name="get_menus"),
    path(
        "menu/<int:id>/details",
        emenu.menu_details.MenuDetailsView.as_view(),
        name="get_menu_details",
    ),
    path("menus/", include((router.urls, "emenu"), namespace="menus")),
]
