from rest_framework import serializers
from .models import User, UserService, Service, Order


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'name', 'role', 'password', 'price', 'phone_number')


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'
