import json

from channels.generic.websocket import AsyncWebsocketConsumer


class TripConsumer(AsyncWebsocketConsumer):
  async def connect(self):
    await self.accept()

  async def disconnect(self, close_code):
    pass

  async def receive(self, text_data):
    data = json.loads(text_data)
    # Handle received data
    await self.send(text_data=json.dumps({"message": "Received"}))
