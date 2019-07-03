from django.contrib import admin

# Register your models here.
from farmer.models import Farmer, Ethnicity

admin.site.register(Farmer)
admin.site.register(Ethnicity)
