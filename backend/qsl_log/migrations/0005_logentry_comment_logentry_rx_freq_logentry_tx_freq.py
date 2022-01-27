# Generated by Django 4.0.1 on 2022-01-27 02:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qsl_log', '0004_logentry_mode'),
    ]

    operations = [
        migrations.AddField(
            model_name='logentry',
            name='comment',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='logentry',
            name='rx_freq',
            field=models.FloatField(help_text='Receiving frequency', null=True),
        ),
        migrations.AddField(
            model_name='logentry',
            name='tx_freq',
            field=models.FloatField(help_text='Transmitting frequency', null=True),
        ),
    ]