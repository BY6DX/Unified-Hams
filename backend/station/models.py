from django.db import models
from user.models import User

class Station(models.Model):
    id = models.AutoField(primary_key=True)
    callsign = models.CharField(max_length=10, null=False, blank=False, help_text="Callsign")
    location = models.CharField(max_length=10, null=False, blank=True, help_text="Maidenhead grid")

    def __str__(self) -> str:
        return f"{self.callsign}"

class HomeStation(Station):
    operators = models.ManyToManyField(User, help_text='Operators of this station')

class Antenna(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30, null=False, blank=False, help_text="Antenna name")

    def __str__(self) -> str:
        return f"{self.name}"

class Transceiver(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30, null=False, blank=False, help_text="Transceiver name")