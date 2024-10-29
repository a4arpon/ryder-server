from rest_framework import serializers

from .models import Driver, Passenger


class DriverSerializer(serializers.ModelSerializer):
  class Meta:
    model = Driver
    fields = ['id', 'driverID', 'name', 'email', 'phone_number', 'driving_license']


class PassengerSerializer(serializers.ModelSerializer):
  class Meta:
    model = Passenger
    fields = ['id', 'userID', 'name', 'email', 'phone']
