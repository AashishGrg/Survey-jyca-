from django.db import models


class Municipality(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Group(models.Model):
    name = models.CharField(max_length=100)
    municipality = models.ForeignKey(Municipality, on_delete=models.CASCADE, related_name="group_municipality")

    def __str__(self):
        return f"{self.name}, {self.municipality.name}"
