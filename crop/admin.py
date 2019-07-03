from django.contrib import admin

from .models import CropName, Crop, CropMethod, CropArea

# Register your models here.
admin.site.register(CropName)
admin.site.register(Crop)
admin.site.register(CropArea)
admin.site.register(CropMethod)
