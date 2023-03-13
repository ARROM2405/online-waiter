from django.contrib.auth.models import User
from django.db import models


class Staff(models.Model):
    user = models.OneToOneField(to=User, on_delete=models.CASCADE)

    class Meta:
        abstract = True


class Waiter(Staff):
    pass


# TODO: Think how to implement archived staff
