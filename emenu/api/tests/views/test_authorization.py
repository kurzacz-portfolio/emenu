from http import HTTPStatus

from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient
from api.tests.custom_test_cases import AuthorizedTestCase


class InvalidateTokenView(AuthorizedTestCase):

    def test_invalidate_token(self):
        # WHEN
        response = self.client.post(reverse("invalidate_token"))

        # THEN
        self.assertEqual(response.status_code, HTTPStatus.OK)
