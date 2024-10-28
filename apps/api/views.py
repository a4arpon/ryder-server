from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Driver
from .serializers import DriverSerializer


def index(request):
  return JsonResponse({
    "message": "Hello World"
  })


@api_view(['POST'])
def create_driver(request):
  serializer = DriverSerializer(data=request.data)
  if serializer.is_valid():
    serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)
  return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_drivers(request):
  drivers = Driver.objects.all()
  serializer = DriverSerializer(drivers, many=True)
  return Response(serializer.data)
