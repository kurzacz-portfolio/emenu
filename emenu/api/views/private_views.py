from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView


class Invalidate(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, format=None):
        self.request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)
