from django.contrib import admin

from .models import Group, Municipality

# Register your models here.
admin.site.register(Municipality)
admin.site.register(Group)
