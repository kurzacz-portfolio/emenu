from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from api.models import Menu
from api.serializers import MenuDetailsSerializer, MenuSerializer
from rest_framework.decorators import action


class InvalidateToken(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, format=None):
        self.request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)


class MenuViewSet(ModelViewSet):

    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

