# Generated by Django 3.1.1 on 2020-10-25 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0001_menu_and_dish"),
    ]

    operations = [
        migrations.AlterField(
            model_name="dish", name="name", field=models.CharField(max_length=63),
        ),
        migrations.AlterUniqueTogether(name="dish", unique_together={("menu", "name")},),
    ]
