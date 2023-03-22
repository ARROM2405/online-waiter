from django.contrib import admin
from orders.models import Table, Order


@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    list_display = ("number",)
    list_filter = ("number",)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        "payment_status",
        "preparation_status",
        "table",
        "waiter",
    )
    list_filter = (
        "payment_status",
        "preparation_status",
        "table",
        "waiter",
    )
