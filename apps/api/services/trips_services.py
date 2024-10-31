from rest_framework import status
from rest_framework.response import Response

from apps.api.models import Trip
from apps.api.serializers import TripSerializer, TripSerializerWithDriverName, TripSerializerWithAllInfo


def create_trip_service(body):
  print(body)
  serializer = TripSerializer(data=body)
  if serializer.is_valid():
    serializer.save()
    return Response({
      "status": 201,
      "success": True,
      "message": "Trip created successfully",
      "data": serializer.data
    }, status=status.HTTP_201_CREATED)

  return Response({
    "status": 400,
    "success": False,
    "message": "Failed to create trip",
    "data": serializer.errors
  }, status=status.HTTP_400_BAD_REQUEST)


def get_all_trips_service():
  try:
    trips = Trip.objects.all()
    trips_data = TripSerializerWithDriverName(trips, many=True).data
    return Response({
      "status": 200,
      "success": True,
      "message": "Trips found successfully",
      "data": trips_data,
    }, status=status.HTTP_200_OK)

  except Exception as e:
    return Response({
      "status": 500,
      "success": False,
      "message": "Internal server error",
      "data": None
    }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


def get_trip_service(trip_id):
  try:
    trip = Trip.objects.select_related('driver', 'passenger').get(
      tripID=trip_id)
    trip_data = TripSerializerWithAllInfo(trip).data
    return Response({
      "status": 200,
      "success": True,
      "message": "Trip found successfully",
      "data": trip_data
    }, status=status.HTTP_200_OK)

  except Trip.DoesNotExist:
    return Response({
      "status": 404,
      "success": False,
      "message": "Trip not found",
      "data": None
    }, status=status.HTTP_404_NOT_FOUND)

  except Exception as e:
    return Response({
      "status": 500,
      "success": False,
      "message": "Internal server error",
      "data": None
    }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
