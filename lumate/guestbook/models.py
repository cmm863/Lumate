from django.db import models


# Create your models here.
class Guest(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    ip_address = models.CharField(max_length=100)
    browser_info = models.CharField(max_length=200)
    date_signed = models.DateField()

