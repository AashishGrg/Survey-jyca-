from rest_framework.serializers import ModelSerializer

from crop.models import Crop


class CropSerializer(ModelSerializer):
    class Meta:
        model = Crop
        fields = ['name', 'area_type', 'method', 'growing_period_from', 'growing_period_to', 'variety', 'area',
                  'production_in_kg', 'sales_in_kg', 'cost', 'general_cost', 'labor_cost', 'other_cost']
