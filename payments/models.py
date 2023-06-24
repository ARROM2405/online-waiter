from django.db import models

from orders.models import Order


class Tip(models.Model):
    order = models.OneToOneField(to=Order, on_delete=models.CASCADE, related_name="tip")
    amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True)
