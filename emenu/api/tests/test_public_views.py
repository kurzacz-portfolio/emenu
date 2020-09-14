from django.test import TestCase
from api.models import Menu, Dish
from django.urls import reverse
from api.serializers import MenuSerializer
from http import HTTPStatus


class MenusListView(TestCase):
    def setUp(self):
        Menu.objects.create(name="Menu 1", description="Menu description 1")
        Menu.objects.create(name="Menu 2", description="Menu description 2")

    def test_get_all_menus(self):
        response = self.client.get(reverse("get_menus"))
        menus = Menu.objects.all()
        serializer = MenuSerializer(menus, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, HTTPStatus.OK)
