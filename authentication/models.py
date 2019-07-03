from django.contrib.auth.models import AbstractUser
from django.db import models

from farmer.models import Ethnicity


class DataCollector(AbstractUser):
    GENDER_TYPE = (('MALE', 'Male'),
                   ('FEMALE', 'Female'),
                   ('OTHER', 'Other'))
    full_name = models.CharField(max_length=50)
    email = models.EmailField(null=True, blank=True)
    gender = models.CharField(max_length=25, choices=GENDER_TYPE, default='MALE')
    ethnicity = models.ForeignKey(Ethnicity, on_delete=models.CASCADE, related_name='data_collector_ethnicity',
                                  null=True, blank=True)
    phone = models.CharField(max_length=50)
    date_of_birth = models.DateField(blank=True, null=True)
    citizenship_number = models.CharField(max_length=100)
    current_address = models.CharField(max_length=100)
    permanent_address = models.CharField(max_length=100)

    def __str__(self):
        return self.username
