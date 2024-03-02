from django.contrib import admin
from .models import User, UserService, Service, Order
# Register your models here.
admin.site.register(User)
admin.site.register(Service)
admin.site.register(UserService)
admin.site.register(Order)