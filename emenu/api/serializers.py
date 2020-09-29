from rest_framework import serializers

from api.models import Dish, Menu


class MenuSerializer(serializers.ModelSerializer):
    dishes_count = serializers.SerializerMethodField()

    class Meta:
        model = Menu
        fields = ["name", "description", "created_at", "updated_at", "dishes_count"]

    def get_dishes_count(self, obj: Menu) -> int:
        return obj.dishes.count()


class DishSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dish
        fields = [
            "description",
            "price",
            "prepare_time",
            "created_at",
            "updated_at",
            "is_vegan",
        ]


class MenuDetailsSerializer(MenuSerializer):
    dishes = DishSerializer(many=True)

    class Meta:
        model = Menu
        fields = [
            "name",
            "description",
            "created_at",
            "updated_at",
            "dishes",
            "dishes_count",
        ]
