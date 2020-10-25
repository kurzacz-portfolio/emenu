from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import MethodNotAllowed

from api.models import Dish
from api.serializers import DishSerializer


class DishViewSet(ModelViewSet):

    queryset = Dish.objects.all()
    serializer_class = DishSerializer
    permission_classes = [IsAuthenticated]

    def list(self, request, *args, **kwargs):
        raise MethodNotAllowed(
            "Listing all dishes is not allowed. "
            "Use menu endpoint to list dishes assigned to a given menu."
        )
