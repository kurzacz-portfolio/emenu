from http import HTTPStatus

from django.test import TestCase
from django.urls import reverse

from api.models import Dish, Menu
from api.serializers import MenuDetailsSerializer


class MenuDetailView(TestCase):
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

    def test_menu_details(self):
        # GIVEN
        menu = self.menu
        serializer = MenuDetailsSerializer(menu)

        # WHEN
        response = self.client.get(reverse("get_menu_details", kwargs={"id": menu.id}))

        # THEN
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, HTTPStatus.OK)
