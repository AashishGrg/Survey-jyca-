from django.db import models

from municipality.models import Municipality, Group


class Ethnicity(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Farmer(models.Model):
    GENDER_TYPE = (('MALE', 'Male'),
                   ('FEMALE', 'Female'),
                   ('OTHER', 'Other'))
    full_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    gender = models.CharField(max_length=25, choices=GENDER_TYPE, default='MALE')
    family_members_count = models.PositiveIntegerField(default=None)
    family_workers_count = models.PositiveIntegerField(default=None)
    municipality = models.ForeignKey(Municipality, on_delete=models.CASCADE, related_name='farmer_municipality')
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='farmer_group')
    ethnicity = models.ForeignKey(Ethnicity, on_delete=models.CASCADE, related_name='farmer_ethnicity')

    def __str__(self):
        return self.full_name
