from django.contrib import admin

from food_and_beverage.models import Food, Beverage


@admin.register(Food)
class DishAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "price",
        "units_available",
    )
    list_filter = (
        "name",
        "price",
        "units_available",
    )
    search_fields = ("name",)


@admin.register(Beverage)
class BeverageAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "price",
        "units_available",
    )
    list_filter = (
        "name",
        "price",
        "units_available",
    )
    search_fields = ("name",)
