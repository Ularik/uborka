from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import User, Service, UserService, Order
from .serializer import UserSerializer, ServiceSerializer


# Create your views here.
@api_view(['GET', 'POST'])
def users(request):
    if request.method == 'GET':
        users_all = User.objects.all()
        serializer = UserSerializer(users_all, many=True)
        print(serializer.data)
        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == 'POST':
        new_user = UserSerializer(data=request.data)
        if new_user.is_valid(raise_exception=True):
            new_user.save()
            return Response(new_user, status=status.HTTP_201_CREATED)


@api_view(['GET', 'POST'])
def service(request):
    if request.method == 'GET':
        service_all = Service.objects.all()
        serializer = ServiceSerializer(service_all, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == 'POST':
        new_service = ServiceSerializer(data=request.data)
        if new_service.is_valid(raise_exception=True):
            new_service.save()
            return Response(new_service, status=status.HTTP_201_CREATED)
