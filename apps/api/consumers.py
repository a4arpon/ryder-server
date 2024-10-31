import json

from channels.generic.websocket import AsyncWebsocketConsumer

from apps.api.services.realtime_services import get_realtime_trip_service


class TripConsumer(AsyncWebsocketConsumer):
  async def connect(self):
    await self.accept()

  async def disconnect(self, close_code):
    pass

  async def receive(self, text_data):
    data = json.loads(text_data)
    trip_id = data.get("trip-id")

    trip = await get_realtime_trip_service(trip_id)
    await self.send(text_data=json.dumps(trip))
