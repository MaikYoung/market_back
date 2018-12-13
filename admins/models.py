
from django.contrib.auth.models import AbstractUser
from django.db import models


class Admin(AbstractUser):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    username = models.CharField(unique=True, max_length=100, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    phone = models.CharField(max_length=20, null=True)
    password = models.CharField(max_length=255)

    def __str__(self):
        return self.email
