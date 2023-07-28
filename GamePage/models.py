from django.contrib.auth.models import User
from django.db import models


class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    Balance = models.IntegerField(default=1000)
def __str__(self):
    return self.user.username
