from atexit import register
from django.contrib import admin
from .models import Plant, UserPlant

# Register your models here.
admin.site.register(Plant)
admin.site.register(UserPlant)
