from api.serializers import MenuSerializer
from api.models import Menu
from rest_framework.generics import ListAPIView
from django_filters.rest_framework import DjangoFilterBackend


class MenusListView(ListAPIView):
    """ View to list menus in the app. """

    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name', 'created_at', "updated_at"]

