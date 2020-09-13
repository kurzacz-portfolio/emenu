from api.serializers import MenuSerializer
from api.models import Menu
from rest_framework.generics import GenericAPIView
from rest_framework import mixins


class MenusView(mixins.ListModelMixin, GenericAPIView):
    """ View to list menus in the app. """

    serializer_class = MenuSerializer
    queryset = Menu.objects.all()

    def get(self, request, *args, **kwargs):
        """ Returns a list of menus. """
        return self.list(request, *args, **kwargs)
