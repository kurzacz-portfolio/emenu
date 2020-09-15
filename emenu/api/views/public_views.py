from api.serializers import MenuSerializer
from api.models import Menu
from rest_framework.generics import ListAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from django.db.models import Count


class MenusListView(ListAPIView):
    """ View to list menus in the app. """

    queryset = Menu.objects.annotate(dishes_count=Count("dishes")).order_by("id")
    serializer_class = MenuSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ["name", "created_at", "updated_at"]
    ordering_fields = ["name", "dishes_count"]
