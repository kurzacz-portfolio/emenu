from django.db import models


class Menu(models.Model):
    name = models.CharField(max_length=63, unique=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Dish(models.Model):
    menu = models.ForeignKey(Menu, related_name="dishes", on_delete=models.CASCADE)
    description = models.TextField()
    price = models.DecimalField(max_digits=4, decimal_places=2)
    prepare_time = models.IntegerField()  # in minutes
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_vegan = models.BooleanField()
