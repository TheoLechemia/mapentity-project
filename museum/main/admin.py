from django.contrib import admin
from leaflet.admin import LeafletGeoAdmin
from .models import Museum

admin.site.register(Museum, LeafletGeoAdmin)