import json

import redis
from asgiref.sync import sync_to_async

from apps.api.models import Trip

redis_client = redis.Redis(host='127.0.0.1', port=6379, db=0, password='userP@ssw0rd')


@sync_to_async
def get_driver_location_service(driver_id):
  driver_key = f"driver-cache:{driver_id}"
  driver_data = redis_client.get(driver_key)

  return driver_data


@sync_to_async
def get_realtime_trip_service(trip_id):
  trip_key = f"trip-cache:{trip_id}"
  trip_data = redis_client.get(trip_key)

  if trip_data:
    trip_data = json.loads(trip_data)
  else:
    try:
      trip = Trip.objects.select_related("driver", "passenger").get(tripID=trip_id)
      trip_data = {
        "currentLocationLat": trip.currentLocationLat,
        "currentLocationLong": trip.currentLocationLong,
        "lastChecked": trip.lastChecked.isoformat() if trip.lastChecked else None,
        "tripStatus": trip.tripStatus,
        "driverID": trip.driver.driverID,
        "passengerID": trip.passenger.userID if trip.passenger else None,
      }
      # Save the trip data in Redis cache
      redis_client.set(trip_key, json.dumps(trip_data))

      # Save the trip ID under a driver-specific key
      driver_key = f"driver-cache:{trip.driver.driverID}"
      redis_client.set(driver_key, trip_id)

    except Trip.DoesNotExist:
      trip_data = {"error": "Trip not found"}

  return trip_data
