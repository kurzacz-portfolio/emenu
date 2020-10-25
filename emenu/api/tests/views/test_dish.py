from http import HTTPStatus

from django.test import TestCase
from django.urls import reverse

from api.models import Dish, Menu
from api.serializers import DishSerializer


class PublicDishViewTest(TestCase):
    def setUp(self):
        self.menu = Menu.objects.create(name="Test menu")

        self.dishes = [
            Dish.objects.create(
                menu=self.menu,
                name="Dish 1",
                description="foo",
                price=15.99,
                prepare_time=15,
                is_vegan=True,
            ),
            Dish.objects.create(
                menu=self.menu,
                name="Dish 2",
                description="bar",
                price=20,
                prepare_time=5,
                is_vegan=False,
            ),
            Dish.objects.create(
                menu=self.menu,
                name="Dish 3",
                description="baz",
                price=35.01,
                prepare_time=12,
                is_vegan=True,
            ),
        ]

    def test_list_reject(self):
        # WHEN
        response = self.client.get(reverse("emenu:dish_crud-list"))

        # THEN
        self.assertEqual(response.status_code, HTTPStatus.METHOD_NOT_ALLOWED)

    def test_retrieve_positive(self):
        # GIVEN
        dish = self.dishes[0]
        serializer = DishSerializer(dish)

        # WHEN
        response = self.client.get(
            reverse("emenu:dish_crud-detail", kwargs={"pk": dish.id})
        )

        # THEN
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, HTTPStatus.OK)
