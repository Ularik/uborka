from rest_framework import serializers
from apps.order.models import Order
from apps.user.serializer import UserSerializer
from apps.user.models import User


class OrderListSerializers(serializers.ModelSerializer):
    id_employer = UserSerializer()
    id_worker = UserSerializer()
    class Meta:
        model = Order
        fields = ('id', 'id_employer', 'id_worker', 'status', 'address', 'created_add', 'start_time')


class OrderCreateSerializers(serializers.ModelSerializer):
    id_employer = UserSerializer()
    id_worker = UserSerializer()
    class Meta:
        model = Order
        fields = ('id', 'id_employer', 'id_worker', 'status', 'address', 'created_add', 'start_time')

    def create(self, validated_data):
        employer = validated_data['id_employer']
        worker = validated_data['id_worker']
        status = validated_data['status']
        address = validated_data['address']
        start_time = validated_data['start_time']
        print(employer)

        id_employer, _ = User.objects.get_or_create(**employer)
        id_worker, _ = User.objects.get_or_create(**worker)

        order = Order(id_employer=id_employer, id_worker=id_worker, status=status,
                      address=address, start_time=start_time)
        order.save()
        return order

    def update(self, instance, validated_data):
        pass
