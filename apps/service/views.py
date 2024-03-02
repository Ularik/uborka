from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .models import Service
from .serializers import ServiceListSerializer, ServiceCreateSerializer


class ServiceListView(generics.ListAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceListSerializer


class ServiceCreateView(generics.CreateAPIView):
    serializer_class = ServiceCreateSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

