from django.db.models import Count
from rest_framework.generics import RetrieveAPIView

from api.models import Menu
from api.serializers import MenuDetailsSerializer


class MenuDetailsView(RetrieveAPIView):
    lookup_field = "id"
    serializer_class = MenuDetailsSerializer
    queryset = Menu.objects.annotate(dishes_count=Count("dishes")).order_by("id")
