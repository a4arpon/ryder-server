import json

from channels.generic.websocket import AsyncWebsocketConsumer

from apps.api.services.realtime_services import update_realtime_trip_service, get_realtime_trip_service


class TripConsumer(AsyncWebsocketConsumer):
  async def connect(self):
    await self.accept()

  async def disconnect(self, close_code):
    pass

  async def receive(self, text_data):
    data = json.loads(text_data)
    action_type = data.get("action-type")
    trip_id = data.get("trip-id")

    if action_type == "update-trip-location":
      location_data = {
        "currentLocationLat": data.get("currentLocationLat"),
        "currentLocationLong": data.get("currentLocationLong"),
        "tripStatus": data.get("tripStatus"),
        "driverID": data.get("driverID"),
        "passengerID": data.get("passengerID"),
      }
      update_realtime_trip_service(trip_id, location_data)

    trip = get_realtime_trip_service(trip_id)
    await self.send(text_data=json.dumps(trip))
