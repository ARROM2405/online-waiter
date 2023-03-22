from django.db import models

from orders.models import Order


class Tip(models.Model):
    order = models.OneToOneField(to=Order, on_delete=models.CASCADE, related_name="tip")
    amount = models.PositiveIntegerField(blank=True)
