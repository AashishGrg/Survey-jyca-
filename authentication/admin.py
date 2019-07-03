from django.contrib import admin
from django.contrib.auth.admin import Group
from django.contrib.auth.admin import UserAdmin

from .models import DataCollector

UserAdmin.fieldsets += ('Custom fields set', {'fields': ('full_name', 'gender', 'ethnicity', 'phone',
                                                         'date_of_birth', 'citizenship_number', 'current_address',
                                                         'permanent_address')}),


class CustomUserAdmin(UserAdmin):
    pass


admin.site.register(DataCollector, CustomUserAdmin)
# # Register your models here.
# admin.site.register(DataCollector)

admin.site.unregister(Group)
