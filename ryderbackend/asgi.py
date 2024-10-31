import os

from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
from django.urls import path

from apps.api import consumers

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ryderbackend.settings')

application = ProtocolTypeRouter({
  "http": get_asgi_application(),
  "websocket": URLRouter([
    path("ws/trip_updates/", consumers.TripConsumer.as_asgi()),
  ]),
})
