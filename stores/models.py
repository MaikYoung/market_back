from _decimal import Decimal

from django.contrib.postgres.fields import ArrayField
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from admins.models import Admin


class Store(models.Model):
    manager = models.ForeignKey(Admin, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    lat = models.DecimalField(max_digits=10, decimal_places=6, default=Decimal(0))
    lng = models.DecimalField(max_digits=10, decimal_places=6, default=Decimal(0))
    adress = models.TextField()
    postal_code = models.IntegerField(null=True)
    schedule_open = models.IntegerField()
    schedule_close = models.IntegerField()
    work_days = ArrayField(models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(6)]), null=True,
                           blank=True, help_text="Separate using a comma")
    is_closed = models.BooleanField(default=False)
    twitter = models.CharField(max_length=200)
    facebook = models.CharField(max_length=200)
    instagram = models.CharField(max_length=100)

    def __str__(self):
        return "%s - %s - %s" % (self.id, self.name, self.manager.email)
