from django.db import models
from datetime import date
from django.utils import timezone

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=100)
    role = models.IntegerField(choices=(
                               (1, 'employer'),
                               (2, 'worker'))
    )
    password = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    phone_number = models.IntegerField(max_length=8)

    def __str__(self):
        return self.name