from django.db import models
from apps.user.models import User


class Service(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)

    def __str__(self):
        return self.name

class UserService(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    service = models.ForeignKey(Service, on_delete=models.PROTECT, related_name='service_name')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_active = models.BooleanField()
    description = models.TextField()


