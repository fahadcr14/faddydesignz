from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=100)
    service = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.CharField(max_length=500,default='')
    phone = models.CharField(max_length=100,blank=True)
    responded = models.CharField(max_length=100,default='no')

from datetime import datetime
import pytz
def time_zone():
    utc_time = datetime.now(pytz.utc)

    # Convert the UTC time to a specific time zone
    target_timezone = pytz.timezone('America/Chicago')
    local_time = utc_time.astimezone(target_timezone)

    return local_time
class Analyticsdata(models.Model):
    ip_address = models.GenericIPAddressField(verbose_name='IP Address', unpack_ipv4=True)
    city = models.CharField(max_length=100, verbose_name='City')
    region = models.CharField(max_length=100, verbose_name='Region')
    country = models.CharField(max_length=100, verbose_name='Country')
    time = models.CharField(max_length=100,default=time_zone())
    total_view_count = models.PositiveIntegerField(default=0, verbose_name='Total View Count')
class Realtimedata(models.Model):
    ip_address = models.GenericIPAddressField(verbose_name='IP Address', unpack_ipv4=True)
    time = models.CharField(max_length=100,default=time_zone())
    total_view_count = models.PositiveIntegerField(default=0, verbose_name='Total View Count')

