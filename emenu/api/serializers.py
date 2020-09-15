from rest_framework import serializers

from api.models import Menu


class MenuSerializer(serializers.ModelSerializer):
    dishes_count = serializers.SerializerMethodField()

    class Meta:
        model = Menu
        fields = ["name", "description", "created_at", "updated_at", "dishes_count"]

    def get_dishes_count(self, obj: Menu) -> int:
        return obj.dishes.count()
