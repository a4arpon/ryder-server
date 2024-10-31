from django.contrib import admin

from .models import Driver, Passenger, Trip

admin.site.register(Driver)
admin.site.register(Passenger)
admin.site.register(Trip)
