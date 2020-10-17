from http import HTTPStatus

from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient
from api.models import Dish, Menu
from api.serializers import MenuDetailsSerializer, MenuSerializer

TEST_USER_NAME = "testuser"
TEST_USER_PASS = "12345"


class PublicMenuViewTest(TestCase):
    def setUp(self):
        self.menu = Menu.objects.create(name="Menu 1", description="Menu description 1")

        self.dishes = [
            Dish.objects.create(
                menu=self.menu,
                description="foo",
                price=15.99,
                prepare_time=15,
                is_vegan=True,
            ),
            Dish.objects.create(
                menu=self.menu,
                description="bar",
                price=20,
                prepare_time=5,
                is_vegan=False,
            ),
            Dish.objects.create(
                menu=self.menu,
                description="baz",
                price=35.01,
                prepare_time=12,
                is_vegan=True,
            ),
        ]

    def test_get_all_menus(self):
        # GIVEN
        menus = Menu.objects.all()
        serializer = MenuSerializer(menus, many=True)

        # WHEN
        response = self.client.get(reverse("emenu:menu-crud-list"))

        # THEN
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, HTTPStatus.OK)

