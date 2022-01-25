from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    id = models.AutoField(primary_key=True, help_text='User ID')
    callsign = models.CharField(max_length=10, null=True, blank=False, help_text="Callsign")
