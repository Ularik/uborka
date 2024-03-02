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

class Service(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)

    def __str__(self):
        return self.name

class UserService(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.PROTECT)
    service_id = models.ForeignKey(Service, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    is_active = models.IntegerField(choices=(
        (1, 'true'),
        (2, 'False')
    ))

    def __str__(self):
        return f'{self.user_id.name}-{self.service_id.name}'

class Order(models.Model):
    id_employer = models.ForeignKey(User, on_delete=models.PROTECT, related_name='employer')
    id_worker = models.ForeignKey(User, on_delete=models.CASCADE, related_name='worker')
    status = models.IntegerField(choices=(
        (1, 'have_done'),
        (2, 'hevent_done')
    ))
    address = models.CharField(max_length=100)
    created_add = models.DateField(auto_now_add=True)
    start_time = models.DateField(default=timezone.now())

    def __str__(self):
        return f'{self.pk}'