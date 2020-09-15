from http import HTTPStatus

from django.db.models import Count
from django.test import TestCase
from django.urls import reverse
from parameterized import parameterized

from api.models import Dish, Menu
from api.serializers import MenuSerializer


class MenusListView(TestCase):
    def setUp(self):
        self.menus = [
            Menu.objects.create(name="Menu 1", description="Menu description 1"),
            Menu.objects.create(name="Menu 2", description="Menu description 2"),
        ]
        Dish.objects.create(
            menu=self.menus[1],
            description="foo",
            price=5.99,
            prepare_time=15,
            is_vegan=False,
        )

    def test_get_all_menus(self):
        # GIVEN
        menus = Menu.objects.all()
        serializer = MenuSerializer(menus, many=True)

        # WHEN
        response = self.client.get(reverse("get_menus"))

        # THEN
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, HTTPStatus.OK)

    @parameterized.expand(
        [
            ("ascending", "name"),
            ("descending", "-name"),
        ]
    )
    def test_sort_by_name(self, name, ordering):
        # GIVEN
        menus = Menu.objects.order_by(ordering)
        serializer = MenuSerializer(menus, many=True)

        # WHEN
        response = self.client.get(reverse("get_menus"), {"ordering": ordering})

        # THEN
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, HTTPStatus.OK)

    @parameterized.expand(
        [
            ("ascending", "dishes_count"),
            ("descending", "-dishes_count"),
        ]
    )
    def test_sort_by_dishes_count(self, name, ordering):
        # GIVEN
        menus = Menu.objects.annotate(dishes_count=Count("dishes")).order_by(ordering)
        serializer = MenuSerializer(menus, many=True)

        # WHEN
        response = self.client.get(reverse("get_menus"), {"ordering": ordering})

        # THEN
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_filter_by_name(self):
        # GIVEN
        menu_name = self.menus[0].name
        menus = Menu.objects.filter(name=menu_name)
        serializer = MenuSerializer(menus, many=True)

        # WHEN
        response = self.client.get(reverse("get_menus"), {"name": menu_name})

        # THEN
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_filter_by_created_at(self):
        # GIVEN
        menu_created_at = self.menus[0].created_at
        menus = Menu.objects.filter(created_at=menu_created_at)
        serializer = MenuSerializer(menus, many=True)

        # WHEN
        response = self.client.get(reverse("get_menus"), {"created_at": menu_created_at})

        # THEN
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_filter_by_updated_at(self):
        # GIVEN
        menu_updated_at = self.menus[0].updated_at
        menus = Menu.objects.filter(updated_at=menu_updated_at)
        serializer = MenuSerializer(menus, many=True)

        # WHEN
        response = self.client.get(reverse("get_menus"), {"updated_at": menu_updated_at})

        # THEN
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, HTTPStatus.OK)
