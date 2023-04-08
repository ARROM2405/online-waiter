from django.contrib.auth.models import User
from django.db import models


class Staff(models.Model):
    user = models.OneToOneField(
        to=User,
        on_delete=models.CASCADE,
    )
    currently_employed = models.BooleanField(default=True)

    class Meta:
        abstract = True


class Waiter(Staff):
    def __str__(self):
        return f"Waiter {self.user.username}"


class Manager(Staff):
    def __str__(self):
        return f"Manager {self.user.username}"
