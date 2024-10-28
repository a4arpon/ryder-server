from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
  path("", views.index, name="index"),
  path('admin/', admin.site.urls),
  path('create-driver/', views.create_driver, name='create-driver'),
  path('get-drivers/', views.get_drivers, name='get-drivers'),
]
