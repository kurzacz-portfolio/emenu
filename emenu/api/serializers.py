from rest_framework import serializers

from api.models import Dish, Menu


class MenuSerializer(serializers.ModelSerializer):
    dishes_count = serializers.SerializerMethodField()

    class Meta:
        model = Menu
        fields = "__all__"

    def get_dishes_count(self, obj: Menu) -> int:
        return obj.dishes.count()


class DishSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dish
        fields = "__all__"


class MenuDetailsSerializer(MenuSerializer):
    dishes = DishSerializer(many=True)

    class Meta:
        model = Menu
        fields = "__all__"
