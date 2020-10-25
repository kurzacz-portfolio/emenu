from rest_framework import routers
from api import views

router = routers.DefaultRouter()
router.register(r"menus/", views.MenuViewSet, basename="menu_crud")
router.register(r"dishes/", views.DishViewSet, basename="dish_crud")
