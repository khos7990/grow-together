from datetime import datetime
from django.db import models
from django.contrib.auth.models import User
from psycopg2 import Timestamp

# Create your models here.

class Plant(models.Model):
    scientific_name = models.CharField(max_length=100)
    common_name = models.CharField(max_length=100)
    water_use = models.CharField(max_length=50)
    light = models.CharField(max_length= 50) 
    maintenance = models.CharField(max_length=50)   

    def __str__(self):
        return self.scientific_name
        return self.common_name
        return self.water_use
        return self.light
        return self.maintenance

class Photo (models.Model):
    url = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for: {self.user_id} @{self.url}"
