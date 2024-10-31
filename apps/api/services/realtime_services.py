from datetime import datetime

from django_redis import cache

from apps.api.models import Trip


def update_realtime_trip_service(trip_id, data):
  trip_key = f"trip-cache:{trip_id}"
  data["lastChecked"] = datetime.now().isoformat()
  cache.set(trip_key, data, timeout=None)


def get_realtime_trip_service(trip_id):
  trip_key = f"trip-cache:{trip_id}"
  trip_data = cache.get(trip_key)

  if not trip_data:
    try:
      trip = Trip.objects.get(tripID=trip_id)
      trip_data = {
        "currentLocationLat": trip.currentLocationLat,
        "currentLocationLong": trip.currentLocationLong,
        "lastChecked": trip.lastChecked.isoformat() if trip.lastChecked else None,
        "tripStatus": trip.tripStatus,
        "driverID": trip.driver.driverID,
        "passengerID": trip.passenger.userID if trip.passenger else None,
      }
      cache.set(trip_key, trip_data, timeout=None)
    except Trip.DoesNotExist:
      trip_data = {"error": "Trip not found"}

  return trip_data
