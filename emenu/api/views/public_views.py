from django.db.models import Count
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.generics import ListAPIView, RetrieveAPIView

from api.models import Menu
from api.serializers import MenuDetailsSerializer, MenuSerializer


class MenusListView(ListAPIView):
    """ View to list menus in the app. """

    queryset = Menu.objects.annotate(dishes_count=Count("dishes")).order_by("id")
    serializer_class = MenuSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ["name", "created_at", "updated_at"]
    ordering_fields = ["name", "dishes_count"]


