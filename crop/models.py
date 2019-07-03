from django.db import models

from farmer.models import Farmer


class CropMethod(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class CropArea(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class CropName(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Crop(models.Model):
    MONTHS = (('BAISHAKH', 'Baishakh'),
              ('JETH', 'Jeth'),
              ('ASAR', 'Asar'),
              ('SAWAN', 'Sawan'),
              ('BHADAU', 'Bhadau'),
              ('ASOJ', 'Asoj'),
              ('KARTIK', 'Kartik'),
              ('MANGSIR', 'Mangsir'),
              ('POUSH', 'Poush'),
              ('MAGH', 'Magh'),
              ('FALGUN', 'Falgun'),
              ('CHAITRA', 'Chaitra'))
    name = models.ForeignKey(CropName, on_delete=models.CASCADE, related_name='crop_crop_name')
    area_type = models.ForeignKey(CropArea, on_delete=models.CASCADE, related_name='crop_crop_area')
    method = models.ForeignKey(CropMethod, on_delete=models.CASCADE, related_name='crop_crop_method')
    growing_period_from = models.CharField(max_length=25, choices=MONTHS)
    growing_period_to = models.CharField(max_length=25, choices=MONTHS)
    variety = models.CharField(max_length=50)
    area = models.IntegerField(default=None)
    production_in_kg = models.FloatField(default=None)
    sales_in_kg = models.FloatField(default=None)
    cost = models.FloatField(default=None)
    general_cost = models.FloatField(default=None)
    labor_cost = models.FloatField(default=None)
    other_cost = models.FloatField(default=None)
    farmer = models.ForeignKey(Farmer, on_delete=models.CASCADE, related_name='crop_farmer', null=True, blank=True)

    def __str__(self):
        return f"Crop name: {self.name.name}, method: {self.method}, farmer: {self.farmer.full_name}"
