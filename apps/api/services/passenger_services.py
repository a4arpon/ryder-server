from rest_framework import status
from rest_framework.response import Response

from apps.api.models import Passenger
from apps.api.serializers import PassengerSerializer


def create_passenger_service(body):
  serializer = PassengerSerializer(data=body)
  if serializer.is_valid():
    serializer.save()
    return Response({
      "status": status.HTTP_201_CREATED,
      "success": True,
      "message": "Passenger created successfully",
      "data": serializer.data
    }, status=status.HTTP_201_CREATED)

  return Response({
    "status": status.HTTP_400_BAD_REQUEST,
    "success": False,
    "message": "Validation error",
    "data": None,
    "extra": serializer.errors
  }, status=status.HTTP_400_BAD_REQUEST)


def get_passengers_service():
  try:
    passengers = Passenger.objects.all()
    serializer = PassengerSerializer(passengers, many=True)
    return Response({
      "status": status.HTTP_200_OK,
      "success": True,
      "message": "Passengers retrieved successfully",
      "data": serializer.data
    }, status=status.HTTP_200_OK)

  except Exception as e:
    return Response({
      "status": status.HTTP_500_INTERNAL_SERVER_ERROR,
      "success": False,
      "message": "An error occurred while retrieving passengers",
      "data": None,
      "extra": {"error": str(e)}
    }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


def get_passenger_service(user_id):
  try:
    passenger = Passenger.objects.get(userID=user_id)
    serializer = PassengerSerializer(passenger)
    return Response({
      "status": status.HTTP_200_OK,
      "success": True,
      "message": "Passenger retrieved successfully",
      "data": serializer.data
    }, status=status.HTTP_200_OK)

  except Passenger.DoesNotExist:
    return Response({
      "status": status.HTTP_404_NOT_FOUND,
      "success": False,
      "message": "Passenger not found",
      "data": None
    }, status=status.HTTP_404_NOT_FOUND)

  except Exception as e:
    return Response({
      "status": status.HTTP_500_INTERNAL_SERVER_ERROR,
      "success": False,
      "message": "An error occurred while retrieving the passenger",
      "data": None,
      "extra": {"error": str(e)}
    }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
