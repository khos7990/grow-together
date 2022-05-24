from atexit import register
from django.contrib import admin
from .models import Plant, Photo, UserPlant

# Register your models here.
admin.site.register(Plant)
admin.site.register(Photo)
admin.site.register(UserPlant)