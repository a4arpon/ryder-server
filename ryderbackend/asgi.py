import os

import django
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
from django.urls import path

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ryderbackend.settings')

django.setup()

from apps.api import consumers

application = ProtocolTypeRouter({
  "http": get_asgi_application(),
  "websocket": URLRouter([
    path("ws/trip_updates/", consumers.TripConsumer.as_asgi()),
  ]),
})
