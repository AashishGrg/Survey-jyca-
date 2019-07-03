from django.db import transaction
from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from crop.serializers import CropSerializer
from farmer.serializers import FarmerCreateSerializer


class FarmerCreateView(CreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = FarmerCreateSerializer
    crop_serializer_class = CropSerializer

    def create(self, request, *args, **kwargs):
        request_data = request.data

        try:
            with transaction.atomic():
                for data in request_data:
                    farmer_data = data["farmer"]
                    crops_data = data["crops"]
                    farmer_serializer = self.get_serializer(data=farmer_data)
                    farmer_serializer.is_valid(raise_exception=True)
                    farmer = farmer_serializer.save()
                    for crop_data in crops_data:
                        crop_serializer = self.crop_serializer_class(data=crop_data)
                        crop_serializer.is_valid(raise_exception=True)
                        crop_serializer.validated_data["farmer"] = farmer
                        crop_serializer.save()
        except ValidationError as e:
            return Response({"success": False, "error": e.get_full_details()}, status=status.HTTP_400_BAD_REQUEST)

        # response_data = farmerUtils.get_all_farmers_with_crops()

        return Response({"success": True}, status=status.HTTP_200_OK)
