from crop.models import Crop
from farmer.models import Farmer


def get_all_farmers_with_crops():
    all_farmers_with_crops = {'farmers': []}
    farmers = Farmer.objects.all()
    for farmer in farmers:
        farmer_dict = {
            'id': farmer.id,
            'phone_number': farmer.phone_number,
            'full_name': farmer.full_name,
            'address': farmer.address,
            'gender': farmer.gender,
            'family_members_count': farmer.family_members_count,
            'family_workers_count': farmer.family_workers_count,
            'municipality': {
                'id': farmer.municipality.id,
                'name': farmer.municipality.name
            },
            'group': {
                'id': farmer.group.id,
                'name': farmer.group.name
            },
            'ethnicity': {
                'id': farmer.ethnicity.id,
                'name': farmer.ethnicity.name
            },
            'crops': []
        }
        crops = Crop.objects.filter(farmer=farmer)
        for crop in crops:
            farmer_dict['crops'].append({
                'id': crop.id,
                'name': crop.name.name,
                'area': crop.area,
                'variety': crop.variety,
                'method': crop.method.name,
                'area_type': crop.area_type.name,
                'production_in_kg': crop.production_in_kg,
                'sales_in_kg': crop.sales_in_kg,
                'cost': crop.cost,
                'general_cost': crop.general_cost,
                'labor_cost': crop.labor_cost,
                'other_cost': crop.other_cost,
                'growing_period_from': crop.growing_period_from,
                'growing_period_to': crop.growing_period_to
            })

        all_farmers_with_crops['farmers'].append(farmer_dict)

    print(all_farmers_with_crops)

    return all_farmers_with_crops
