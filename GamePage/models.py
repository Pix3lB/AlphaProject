from django.contrib.auth.models import User
from django.db import models


class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    Balance = models.IntegerField(default=1000)
    Phone_Number = models.CharField(max_length=10,null=True)
def __str__(self):
    return self.user.username
