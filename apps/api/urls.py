from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
  path("", views.index, name="index"),
  path('admin/', admin.site.urls),

  # ----------------------------------------------------------------------
  # Driver API
  # ----------------------------------------------------------------------
  path('create-driver/', views.create_driver, name='create-driver'),
  path('get-drivers/', views.get_drivers, name='get-drivers'),
  path('get-drivers/<str:driverID>/', views.get_driver, name='get-driver'),

  # ----------------------------------------------------------------------
  # Passenger API
  # ----------------------------------------------------------------------
  path('create-passenger/', views.create_passenger, name='create-passenger'),
  path('get-passengers/', views.get_passengers, name='get-passengers'),
  path('get-passengers/<str:user_id>/', views.get_passenger, name='get-passenger'),

  # ----------------------------------------------------------------------
  # Trips API
  # ----------------------------------------------------------------------
  path('create-trip/', views.create_trip, name='create-trip'),
]
