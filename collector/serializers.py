from rest_framework import serializers

from .models import CollectorGroup


class CollectorGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = CollectorGroup
        fields = ('data_collector', 'municipality')

# class FarmerDataSerializer(serializers.ModelSerializer):
#     # municipality = serializers.CharField()
#     # group = serializers.CharField()
#     # area = serializers.CharField()
#     # method = serializers.CharField()
#     # ethnicity = serializers.CharField()


#     class Meta:
#         model = FarmerData
#         fields = ('phone_number', 'full_name', 'address',
#                   'family_members_count', 'family_workers_count', 'ethnicity',
#                   'municipality','group','area','method')

#
# class FarmerDataSerializer(serializers.ModelSerializer):
#     # municipality = serializers.SlugRelatedField(
#     #     many=True,
#     #     queryset=Municipality.objects.all(),
#     #     slug_field='farmer_municipality'
#     # )
#     # group = serializers.SlugRelatedField(
#     #     many=True,
#     #     queryset=Group.objects.all(),
#     #     slug_field='group_name'
#     # )
#     # area = serializers.SlugRelatedField(
#     #     many=True,
#     #     queryset=Area.objects.all(),
#     #     slug_field='name'
#     # )
#     # method = serializers.SlugRelatedField(
#     #     many=True,
#     #     queryset=Method.objects.all(),
#     #     slug_field='name'
#     # )
#     # ethnicity = serializers.SlugRelatedField(
#     #     many=True,
#     #     queryset=Ethnicity.objects.all(),
#     #     slug_field='name'
#     # )
#
#     class Meta:
#         model = FarmerData
#         fields = ('phone_number', 'full_name', 'address', 'family_members_count',
#                   'family_workers_count', 'variety', 'growing_period_from',
#                   'growing_period_to', 'ropani', 'production_in_kg', 'sales_in_kg',
#                   'cost', 'general_cost', 'labour_cost', 'other_cost', 'area',
#                   'municipality', 'group', 'method', 'ethnicity', 'crop')
#
#     def create(self, validated_data):
#         phone_number = validated_data['phone_number']
#         full_name = validated_data['full_name']
#         address = validated_data['address']
#         family_members_count = validated_data[
#             'family_members_count']
#         family_workers_count = validated_data[
#             'family_workers_count']
#         growing_period_to = validated_data[
#             'growing_period_to']
#         growing_period_from = validated_data[
#             'growing_period_from']
#         ethnicity = validated_data['ethnicity']
#         municipality = validated_data['municipality']
#         group = validated_data['group']
#         area = validated_data['area']
#         crop = validated_data['crop']
#         print(area)
#         method = validated_data['method']
#
#         municipality_obj = Municipality.objects.get(name=municipality)
#         group_obj = Group.objects.get(group_name=group)
#         print(group_obj.id)
#         print(municipality_obj.id)
#         area_obj = Area.objects.get(name=area)
#         method_obj = Method.objects.get(method=method)
#         ethnicity_obj=Ethnicity.objects.get(name=ethnicity)
#         farmer_data = FarmerData.objects.create(phone_number=phone_number, full_name=full_name, address=address,
#                                                 family_members_count=family_members_count,
#                                                 family_workers_count=family_workers_count,
#                                                 ethnicity=ethnicity_obj, municipality=municipality_obj,
#                                                 group=group_obj, area=area_obj,crop=crop, method=method_obj,
#                                                 growing_period_from=growing_period_from,growing_period_to=growing_period_to)
#         return farmer_data
#
#
