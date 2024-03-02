from django.db import models
from apps.user.models import User
from django.utils import timezone
# Create your models here.
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