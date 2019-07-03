from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from authentication.models import DataCollector
from .models import CollectorGroup
from .serializers import CollectorGroupSerializer


class CollectorGroupAPIView(ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = CollectorGroupSerializer

    def list(self, request, *args, **kwargs):
        data_collector = DataCollector.objects.get(username=self.request.user)
        data_collector_name = data_collector.full_name
        collector_groups = CollectorGroup.objects.filter(data_collectors=data_collector)
        response = []

        for collector_group in collector_groups:
            groups = collector_group.groups.all()
            for group in groups:
                group_dict = {
                    "municipality": {
                        'id': group.municipality.id,
                        'name': group.municipality.name
                    },
                    "group": {
                        'id': group.id,
                        'name': group.name
                    },
                    "data_collector": data_collector_name
                }
                response.append(group_dict)

        return Response(data=response)
