from rest_framework import serializers
from .models import Service, UserService
from apps.user.models import User
from apps.user.serializer import UserSerializer


class ServiceListSerializer(serializers.ModelSerializer):
    # service_name = serializers.CharField(source='service.name')

    class Meta:
        model = Service
        fields = ('id', 'name', 'description')


class ServiceCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ('id', 'name', 'description')

    def create(self, validated_data):
        service = Service.objects.get_or_create(**validated_data)
        return service

class ServiceUserCreateSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    service = ServiceListSerializer()
    # service_name = serializers.CharField(source='service.name')
    class Meta:
        model = UserService
        fields = ('id', 'user', 'service', 'price', 'is_active', 'description')
    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user, _ = User.objects.get_or_create(**user_data)
        service_data = validated_data.pop('service')
        service, _ = Service.objects.get_or_create(**service_data)
        service = UserService(**validated_data, service=service, user=user)
        service.save()
        return service

    def update(self, instance, validated_data):
        service_data = validated_data.pop('category')
        service = Service.object.get(pk=service_data['id'])
        return super().update(instance, validated_data)


