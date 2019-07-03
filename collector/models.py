from django.db import models

from authentication.models import DataCollector
from municipality.models import Group


class CollectorGroup(models.Model):
    data_collectors = models.ManyToManyField(DataCollector, related_name='collector_group_data_collector')
    groups = models.ManyToManyField(Group, related_name='collector_group_group')

    def __str__(self):
        return f"Collector Group {self.id}"
