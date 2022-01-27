from ast import operator
from django.db import models
from station.models import Antenna, Station, HomeStation, Transceiver
from user.models import User

class LogEntry(models.Model):
    id = models.AutoField(primary_key=True)
    datetime = models.DateTimeField(help_text='Datetime for the QSL')
    station = models.ForeignKey(HomeStation, on_delete=models.SET_NULL, null=True, related_name='log_entry_as_home')
    antenna = models.ForeignKey(Antenna, on_delete=models.SET_NULL, null=True, related_name='log_entry_as_home')
    transceiver = models.ForeignKey(Transceiver, on_delete=models.SET_NULL, null=True, related_name='log_entry_as_home')
    power = models.FloatField(null=True, help_text='Our power used (Watt)')
    signal_report = models.CharField(max_length=10, help_text='Signal report given by us')
    operator = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name="logs_operated")
    mode = models.CharField(max_length=20, help_text='Operating mode')
    tx_freq = models.FloatField(null=True, help_text='Transmitting frequency')
    rx_freq = models.FloatField(null=True, help_text='Receiving frequency')

    remote_station = models.ForeignKey(Station, on_delete=models.SET_NULL, null=True, related_name='log_entry_as_remote')
    remote_antenna = models.ForeignKey(Antenna, on_delete=models.SET_NULL, null=True, related_name='log_entry_as_remote')
    remote_transceiver = models.ForeignKey(Transceiver, on_delete=models.SET_NULL, null=True, related_name='log_entry_as_remote')
    remote_power = models.FloatField(null=True, help_text='Remote power used (Watt)')
    remote_signal_report = models.CharField(max_length=10, help_text='Signal report given by them')

    comment = models.TextField(null=True)
