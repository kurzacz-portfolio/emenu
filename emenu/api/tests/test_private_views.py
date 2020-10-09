from http import HTTPStatus

from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient


TEST_USER_NAME = "testuser"
TEST_USER_PASS = "12345"


class InvalidateTokenView(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username=TEST_USER_NAME, password=TEST_USER_PASS
        )
        self.token = Token.objects.create(user=self.user)
        self.client = APIClient()

    def test_invalidate_token(self):
        # GIVEN
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token.key)

        # WHEN
        response = self.client.post(reverse("invalidate_token"))

        # THEN
        self.assertEqual(response.status_code, HTTPStatus.OK)
