from http import HTTPStatus

from django.contrib.auth.models import User
from django.db.models import Count
from django.test import TestCase
from django.urls import reverse
from parameterized import parameterized
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient

from api.models import Dish, Menu
from api.serializers import MenuDetailsSerializer, MenuSerializer
from api.tests.custom_test_cases import AuthorizedTestCase


class PublicMenuViewTest(TestCase):
    def setUp(self):
        self.menus = [
            Menu.objects.create(name="Menu 1", description="Menu description 1"),
            Menu.objects.create(name="Menu 2", description="Menu description 2"),
        ]

        self.dishes = [
            Dish.objects.create(
                menu=self.menus[1],
                name="Dish 1",
                description="foo",
                price=15.99,
                prepare_time=15,
                is_vegan=True,
            ),
            Dish.objects.create(
                menu=self.menus[1],
                name="Dish 2",
                description="bar",
                price=20,
                prepare_time=5,
                is_vegan=False,
            ),
            Dish.objects.create(
                menu=self.menus[1],
                name="Dish 3",
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
        response = self.client.get(reverse("emenu:menu_crud-list"))

        # THEN
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, HTTPStatus.OK)

    @parameterized.expand(
        [("ascending", "name"), ("descending", "-name"),]
    )
    def test_sort_by_name(self, name, ordering):
        # GIVEN
        menus = Menu.objects.order_by(ordering)
        serializer = MenuSerializer(menus, many=True)

        # WHEN
        response = self.client.get(
            reverse("emenu:menu_crud-list"), {"ordering": ordering}
        )

        # THEN
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, HTTPStatus.OK)

    @parameterized.expand(
        [("ascending", "dishes_count"), ("descending", "-dishes_count"),]
    )
    def test_sort_by_dishes_count(self, name, ordering):
        # GIVEN
        menus = Menu.objects.annotate(dishes_count=Count("dishes")).order_by(ordering)
        serializer = MenuSerializer(menus, many=True)

        # WHEN
        response = self.client.get(
            reverse("emenu:menu_crud-list"), {"ordering": ordering}
        )

        # THEN
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_filter_by_name(self):
        # GIVEN
        menu_name = self.menus[0].name
        menus = Menu.objects.filter(name=menu_name)
        serializer = MenuSerializer(menus, many=True)

        # WHEN
        response = self.client.get(reverse("emenu:menu_crud-list"), {"name": menu_name})

        # THEN
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_filter_by_created_at(self):
        # GIVEN
        menu_created_at = self.menus[0].created_at
        menus = Menu.objects.filter(created_at=menu_created_at)
        serializer = MenuSerializer(menus, many=True)

        # WHEN
        response = self.client.get(
            reverse("emenu:menu_crud-list"), {"created_at": menu_created_at}
        )

        # THEN
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_filter_by_updated_at(self):
        # GIVEN
        menu_updated_at = self.menus[0].updated_at
        menus = Menu.objects.filter(updated_at=menu_updated_at)
        serializer = MenuSerializer(menus, many=True)

        # WHEN
        response = self.client.get(
            reverse("emenu:menu_crud-list"), {"updated_at": menu_updated_at}
        )

        # THEN
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, HTTPStatus.OK)


class AuthorizedMenuViewTest(AuthorizedTestCase):
    def test_create_positive(self):
        # GIVEN
        create_payload = {
            "name": "Test menu name",
            "description": "Test description",
        }

        # WHEN
        response = self.client.post(
            reverse("emenu:menu_crud-list"), create_payload, format="json"
        )

        # THEN
        self.assertEqual(response.status_code, HTTPStatus.CREATED)

    def test_create_reject_blank_menu_name(self):
        # GIVEN
        create_payload = {
            "name": "",
            "description": "Test description",
        }

        # WHEN
        response = self.client.post(
            reverse("emenu:menu_crud-list"), create_payload, format="json"
        )

        # THEN
        self.assertEqual(response.status_code, HTTPStatus.BAD_REQUEST)

    def test_update_positive(self):
        # GIVEN
        menu = Menu.objects.create(name="Test Menu", description="Test description")
        changed_name = "Changed menu name"
        update_payload = {
            "name": changed_name,
            "description": "Test description",
        }

        # WHEN
        response = self.client.put(
            reverse("emenu:menu_crud-detail", kwargs={"pk": menu.id}),
            update_payload,
            format="json",
        )

        # THEN
        self.assertEqual(response.status_code, HTTPStatus.OK)
