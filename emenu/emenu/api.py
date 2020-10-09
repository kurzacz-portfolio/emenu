from rest_framework import routers
from api.views import private_views

router = routers.DefaultRouter()
router.register(r'menucrud', private_views.MenuViewSet)
