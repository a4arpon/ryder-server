from django.http import JsonResponse
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.decorators import api_view

from .serializers import TripSerializer
from .services.driver_services import create_driver_service, get_drivers_service, get_driver_service
from .services.passenger_services import get_passengers_service, get_passenger_service, create_passenger_service
from .services.trips_services import create_trip_service, get_all_trips_service, get_trip_service


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


# -------------------------------------------------------------------------
#
# Trip API
#
# Methods:
#   - POST /api/create-trip/
#   - GET /api/get-trips/
#   - GET /api/get-trip/:trip_id
# -------------------------------------------------------------------------


@swagger_auto_schema(
  method='post',
  request_body=TripSerializer,
  responses={
    201: TripSerializer,
    400: openapi.Response(description="Bad Request")
  }
)
@api_view(['POST'])
def create_trip(request):
  return create_trip_service(request.body)


@api_view(['GET'])
def get_all_trips(request):
  return get_all_trips_service()


@api_view(['GET'])
def get_trip(request, trip_id):
  return get_trip_service(trip_id)
