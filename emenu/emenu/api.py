from rest_framework import routers
from api.views import menu

router = routers.DefaultRouter()
router.register(r"", menu.MenuViewSet, basename="menu_crud")
