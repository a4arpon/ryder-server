from django_redis import cache


def update_realtime_trip_service():
  trip_data = {
    "tripID": "rfwerwe",
    "startedFrom": "Dhaka",
    "startedFromLat": "23.7104",
    "startedFromLong": "90.4071",
    "startingTime": "2024-10-29T12:34:56",  # Example ISO format time
    "currentLocationLat": "23.8121",
    "currentLocationLong": "90.4198",
    "tripStatus": "active"
  }
  cache.set(f"trip:{trip_data['tripID']}", trip_data, timeout=None)


def get_realtime_trip_service(trip_id):
  return cache.get(f"trip:{trip_id}")
