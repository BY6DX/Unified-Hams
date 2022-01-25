from django.contrib import admin
from .models import Station, HomeStation, Antenna, Transceiver

# Register your models here.
admin.site.register(Station)
admin.site.register(HomeStation)
admin.site.register(Antenna)
admin.site.register(Transceiver)