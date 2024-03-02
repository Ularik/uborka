
from django.contrib import admin
from django.urls import path
from .views import users, service

urlpatterns = [
    path('users/', users),
    path('service/', service),
]
