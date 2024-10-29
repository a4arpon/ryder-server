from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view

from .services.driver_services import create_driver_service, get_drivers_service, get_driver_service
from .services.passenger_services import get_passengers_service, get_passenger_service, create_passenger_service


def index(request):
  return JsonResponse({
    "status": status.HTTP_200_OK,
    "success": True,
    "message": "Hello World",
    "data": []
  })


# -------------------------------------------------------------------------
#
# Driver API
#
# Methods:
#   - POST /api/create-driver/
#   - GET /api/get-drivers/
#   - GET /api/get-driver/
# -------------------------------------------------------------------------

@api_view(['POST'])
def create_driver(request):
  return create_driver_service(request.body)


@api_view(['GET'])
def get_drivers(request):
  return get_drivers_service()


@api_view(['GET'])
def get_driver(request, driverID):
  return get_driver_service(driverID)


# -------------------------------------------------------------------------
#
# Passenger API
#
# Methods:
#   - POST /api/create-passenger/
#   - GET /api/get-passengers/
#   - GET /api/get-passenger/:user_id
# -------------------------------------------------------------------------

@api_view(['POST'])
def create_passenger(request):
  return create_passenger_service(request.body)


@api_view(['GET'])
def get_passengers(request):
  return get_passengers_service()


@api_view(['GET'])
def get_passenger(request, user_id):
  return get_passenger_service(user_id)
