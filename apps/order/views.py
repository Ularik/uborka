from rest_framework import generics
from apps.default.models import Order
from .serializers import OrderListSerializers, OrderCreateSerializers


class OrderListView(generics.ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderListSerializers


class OrderCreateView(generics.CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderCreateSerializers
