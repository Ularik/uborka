from rest_framework import serializers
from apps.default.models import Order


class OrderListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('status','address', 'created_at', 'start_time')


class OrderCreateSerializers(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('id', 'status', 'address', 'start_time')

    def create(self, validated_data):

        order = Order(**validated_data)
        order.save()
        return order

    def update(self, instance, validated_data):
        pass
