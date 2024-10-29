import secrets
import string

from django.db import models


def generate_unique_id():
  return ''.join(secrets.choice(string.ascii_uppercase + string.digits) for _ in range(6))


class Driver(models.Model):
  STATUS_CHOICES = [
    ('available', 'Available'),
    ('on_trip', 'On Trip'),
    ('offline', 'Offline'),
    ('idle', 'Idle'),
  ]

  TRIP_STATUS_CHOICES = [
    ('way_to_pickup', 'Way to Pick Up'),
    ('reached_pickup', 'Reached Pickup'),
    ('way_to_dropoff', 'Way to Drop Off'),
  ]

  driverID = models.CharField(max_length=10, null=True)
  name = models.CharField(max_length=100)
  email = models.EmailField(unique=True, default="UNKNOWN")
  phone_number = models.CharField(max_length=15, unique=True, default="UNKNOWN")
  driving_license = models.CharField(max_length=50, unique=True, default="UNKNOWN")
  balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
  last_trip_location = models.CharField(max_length=255, blank=True, null=True)
  today_started_at = models.DateTimeField(blank=True, null=True)
  last_trip_end_at = models.DateTimeField(blank=True, null=True)
  status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='offline')
  trip_status = models.CharField(max_length=20, choices=TRIP_STATUS_CHOICES, blank=True, null=True)

  def save(self, *args, **kwargs):
    if not self.driverID:
      self.driverID = generate_unique_id()
    super().save(*args, **kwargs)

  def __str__(self):
    return self.name


class Passenger(models.Model):
  userID = models.CharField(max_length=10, null=True)
  name = models.CharField(max_length=100)
  email = models.EmailField(unique=True)
  phone = models.CharField(max_length=15, unique=True)

  def save(self, *args, **kwargs):
    if not self.userID:
      self.userID = generate_unique_id()
    super(Passenger, self).save(*args, **kwargs)

  def __str__(self):
    return self.name


class Trip(models.Model):
  TRIP_STATUS_CHOICES = [
    ('waiting_for_passenger', 'Waiting for Passenger'),
    ('completed', 'Completed'),
    ('rejected', 'Rejected'),
    ('way_to_pick_up', 'Way to Pick Up'),
    ('cancelled', 'Cancelled'),
    ('way_to_drop_off', 'Way to Drop Off'),
  ]

  tripID = models.CharField(max_length=10, null=True)
  driver = models.ForeignKey(Driver, on_delete=models.CASCADE, related_name='trips')
  tripFee = models.DecimalField(max_digits=10, decimal_places=2)
  driversEarning = models.DecimalField(max_digits=10, decimal_places=2)
  startedFrom = models.CharField(max_length=255)
  startedFromLat = models.CharField(max_length=20)
  startedFromLong = models.CharField(max_length=20)
  startingTime = models.DateTimeField()
  passenger = models.ForeignKey(Passenger, on_delete=models.SET_NULL, null=True, related_name='trips')
  currentLocationLat = models.CharField(max_length=20, blank=True, null=True)
  currentLocationLong = models.CharField(max_length=20, blank=True, null=True)
  destination = models.CharField(max_length=255)
  destinationLat = models.CharField(max_length=20)
  destinationLong = models.CharField(max_length=20)
  lastChecked = models.DateTimeField(blank=True, null=True)
  tripStatus = models.CharField(max_length=25, choices=TRIP_STATUS_CHOICES, default='waiting_for_passenger')
  createdAt = models.DateTimeField(auto_now_add=True)
  updatedAt = models.DateTimeField(auto_now=True)

  def save(self, *args, **kwargs):
    if not self.tripID:
      self.tripID = generate_unique_id()
    super().save(*args, **kwargs)

  def __str__(self):
    return f"Trip {self.tripID} by Driver {self.driver.name}"
