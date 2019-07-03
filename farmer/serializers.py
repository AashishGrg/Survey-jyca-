from rest_framework.serializers import ModelSerializer

from farmer.models import Farmer


class FarmerSerializer(ModelSerializer):
    class Meta:
        model = Farmer
        fields = '__all__'


class FarmerCreateSerializer(ModelSerializer):
    class Meta:
        model = Farmer
        fields = ['phone_number', 'full_name', 'address', 'gender', 'family_members_count', 'family_workers_count',
                  'municipality', 'group', 'ethnicity']
