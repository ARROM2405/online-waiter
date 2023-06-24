# Generated by Django 4.1.7 on 2023-05-08 04:53

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("orders", "0002_alter_order_table_alter_order_waiter"),
        ("food_and_beverage", "0003_rename_dish_food"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="beverage",
            name="order",
        ),
        migrations.RemoveField(
            model_name="food",
            name="order",
        ),
        migrations.AddField(
            model_name="beverage",
            name="orders",
            field=models.ManyToManyField(blank=True, to="orders.order"),
        ),
        migrations.AddField(
            model_name="food",
            name="orders",
            field=models.ManyToManyField(blank=True, to="orders.order"),
        ),
        migrations.AlterField(
            model_name="beverage",
            name="name",
            field=models.CharField(max_length=128, unique=True),
        ),
        migrations.AlterField(
            model_name="food",
            name="name",
            field=models.CharField(max_length=128, unique=True),
        ),
    ]
