from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=100)
    role = models.IntegerField(choices=(
                               (1, ''),
                               (2, '')))
    password = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    phone_number = models.IntegerField(max_length=8)

class Service(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)

class UserService(models.Model):
    user_id = models.ForeignKey(User)
    order_id = models.ForeignKey(Service)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    is_active = models.IntegerField(choices=(
        (1, 'true'),
        (2, 'False')
    ))

class Order(models.Model):
    id_customer = models.ForeignKey(User)
    id_worker = models.ForeignKey()
    status = models.IntegerField(choices=(
        (1, 'sdelal'),
        (2, 'nesdelal')
    ))
    address = models.CharField(max_length=100)
    created_add = models.DateField(auto_now_add=True)
    start_time = models.DateField(auto_now=True)