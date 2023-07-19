from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=100)
    service = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.CharField(max_length=500,default='')
    phone = models.CharField(max_length=100,blank=True)
