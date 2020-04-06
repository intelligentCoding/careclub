from django.db import models
from datetime import datetime
# Create your models here.

class Registration(models.Model):
    firstName = models.CharField(max_length = 50)
    lastName = models.CharField(max_length = 50)
    phoneNumber = models.CharField(max_length = 10)
    emailAddress = models.CharField(max_length = 100)
    address = models.CharField(max_length = 500)
    postalCode = models.CharField(max_length = 6)
    province = models.CharField(max_length = 50)
    city = models.CharField(max_length = 50)
    date_joined = models.DateTimeField(default=datetime.now, blank=True)
    def __str__(self):
        return self.firstName