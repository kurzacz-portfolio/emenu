from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from django.db.models import Count

from api.models import Menu
from api.serializers import MenuDetailsSerializer, MenuSerializer
from rest_framework.decorators import action


class MenuViewSet(ModelViewSet):

    queryset = Menu.objects.annotate(dishes_count=Count("dishes")).order_by("id")
    serializer_class = MenuSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ["name", "created_at", "updated_at"]
    ordering_fields = ["name", "dishes_count"]
