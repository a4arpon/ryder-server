from datetime import datetime

from rest_framework import serializers

from .models import Driver, Passenger, Trip


class DriverSerializer(serializers.ModelSerializer):
  class Meta:
    model = Driver
    fields = ['id', 'driverID', 'name', 'email', 'phone_number', 'driving_license', 'balance', 'status', 'trip_status']


class PassengerSerializer(serializers.ModelSerializer):
  class Meta:
    model = Passenger
    fields = ['id', 'userID', 'name', 'email', 'phone']


class TripSerializer(serializers.ModelSerializer):
  class Meta:
    model = Trip
    fields = [
      'driver', 'tripFee', 'driversEarning', 'startedFrom', 'startedFromLat', 'startedFromLong',
      'passenger', 'destination', 'destinationLat', 'destinationLong', 'tripStatus'
    ]

  def create(self, validated_data):
    driversEarning_percentage = validated_data.pop('driversEarning')
    validated_data['driversEarning'] = validated_data['tripFee'] * (driversEarning_percentage / 100)
    validated_data['startingTime'] = datetime.now()
    validated_data['lastChecked'] = datetime.now()
    return super().create(validated_data)


class TripSerializerWithDriverName(serializers.ModelSerializer):
  driver_name = serializers.CharField(source="driver.name", read_only=True)
  driver_id = serializers.CharField(source="driver.driverID", read_only=True)

  class Meta:
    model = Trip
    fields = [
      'tripID', 'driver', 'driver_name', 'tripFee', 'driversEarning', 'startedFrom', 'startedFromLat',
      'startedFromLong', 'passenger', 'destination', 'destinationLat', 'destinationLong', 'tripStatus', 'createdAt',
      'driver_id'
    ]


class TripSerializerWithAllInfo(serializers.ModelSerializer):
  driver = DriverSerializer(read_only=True)
  passenger = PassengerSerializer(read_only=True)

  class Meta:
    model = Trip
    fields = '__all__'
