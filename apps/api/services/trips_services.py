from rest_framework import status
from rest_framework.response import Response

from apps.api.serializers import TripSerializer


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
