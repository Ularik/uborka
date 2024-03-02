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

class OrderSerializer(serializers.ModelSerializer):
    id_employer = UserSerializer()
    id_worker = UserSerializer()
    class Meta:
        model = Order
        fields = ('id', 'id_employer', 'id_worker', 'status', 'address', 'created_add', 'start_time')

    def create(self, validated_data):
        id_employer = validated_data['id_employer']
        id_worker = validated_data['id_worker']
        status = validated_data['status']
        address = validated_data['address']
        start_time = validated_data['start_time']
        employer, _ = User.objects.get_or_create(**id_employer)
        worker, _ = User.objects.get_or_create(**id_worker)
        order = Order(id_employer=employer, id_worker=worker, status=status, address=address, start_time=start_time)
        order.save()
        return order