from rest_framework import serializers
from .models import Service, UserService, User


class ServiceListSerializer(serializers.ModelSerializer):
    service_name = serializers.CharField(source='service.name')

    class Meta:
        model = Service
        fields = ('id', 'name', 'description')


class ServiceCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ('id', 'name', 'description')

    def create(self, validated_data):
        service_data = validated_data.pop('category')
        service, _ = UserService.objects.get_or_create(**service_data)
        service = Service(**validated_data, category=service)
        service.save()
        return service

    def update(self, instance, validated_data):
        service_data = validated_data.pop('category')
        service = Service.object.get(pk=service_data['id'])
        return super().update(instance, validated_data)


