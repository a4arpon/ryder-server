# Generated by Django 5.1.2 on 2024-10-30 06:09

from django.db import migrations, models


class Migration(migrations.Migration):
  dependencies = [
    ('api', '0002_alter_trip_destinationlat_alter_trip_destinationlong_and_more'),
  ]

  operations = [
    migrations.AlterField(
      model_name='trip',
      name='driversEarning',
      field=models.FloatField(),
    ),
    migrations.AlterField(
      model_name='trip',
      name='tripFee',
      field=models.FloatField(),
    ),
  ]
