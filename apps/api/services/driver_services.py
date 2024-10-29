from rest_framework import status
from rest_framework.response import Response

from apps.api.models import Driver
from apps.api.serializers import DriverSerializer


def create_driver_service(body):
  serializer = DriverSerializer(data=body)
  if serializer.is_valid():
    serializer.save()
    return Response({
      "status": status.HTTP_201_CREATED,
      "success": True,
      "message": "Driver created successfully",
      "data": serializer.data
    }, status=status.HTTP_201_CREATED)

  return Response({
    "status": status.HTTP_400_BAD_REQUEST,
    "success": False,
    "message": "Validation error",
    "data": None,
    "extra": serializer.errors
  }, status=status.HTTP_400_BAD_REQUEST)


def get_drivers_service():
  try:
    drivers = Driver.objects.all()
    serializer = DriverSerializer(drivers, many=True)
    return Response({
      "status": status.HTTP_200_OK,
      "success": True,
      "message": "Drivers retrieved successfully",
      "data": serializer.data
    }, status=status.HTTP_200_OK)

  except Exception as e:
    return Response({
      "status": status.HTTP_500_INTERNAL_SERVER_ERROR,
      "success": False,
      "message": "An error occurred while retrieving drivers",
      "data": None,
      "extra": {"error": str(e)}
    }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


def get_driver_service(driver_id):
  try:
    driver = Driver.objects.get(driverID=driver_id)
    serializer = DriverSerializer(driver)
    return Response({
      "status": status.HTTP_200_OK,
      "success": True,
      "message": "Driver retrieved successfully",
      "data": serializer.data
    }, status=status.HTTP_200_OK)

  except Driver.DoesNotExist:
    return Response({
      "status": status.HTTP_404_NOT_FOUND,
      "success": False,
      "message": "Driver not found",
      "data": None
    }, status=status.HTTP_404_NOT_FOUND)

  except Exception as e:
    return Response({
      "status": status.HTTP_500_INTERNAL_SERVER_ERROR,
      "success": False,
      "message": "An error occurred while retrieving the driver",
      "data": None,
      "extra": {"error": str(e)}
    }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
