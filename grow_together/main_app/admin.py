from atexit import register
from django.contrib import admin
from .models import Photo, Plant

# Register your models here.
admin.site.register(Plant)
admin.site.register(Photo)