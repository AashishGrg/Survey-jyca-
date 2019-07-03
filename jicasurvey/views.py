from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from crop.models import CropName, CropMethod, CropArea
from farmer.models import Ethnicity


# class PageViewSet(viewsets.ModelViewSet):
#     """
#         A simple ViewSet for listing or retrieving farmers.
#     """
#     serializer_class = FarmerSerializer
#     queryset = Farmer.objects.all()


class PageViewSet(viewsets.ViewSet):
    """
        A simple ViewSet for listing or retrieving crop areas, crop names, crop methods, ethnicity.
    """
    permission_classes = (IsAuthenticated,)

    def list(self, request, **kwargs):
        # queryset = Farmer.objects.all()
        # serializer = FarmerSerializer(queryset, many=True)
        # return Response(serializer.data)
        response = {
            'crop_areas': CropArea.objects.values(),
            'crop_names': CropName.objects.values(),
            'crop_methods': CropMethod.objects.values(),
            'ethnicity': Ethnicity.objects.values()
        }
        return Response(data=response, status=status.HTTP_200_OK)

    # def retrieve(self, request, pk=None):
    #     queryset = Farmer.objects.all()
    #     user = get_object_or_404(queryset, pk=pk)
    #     serializer = FarmerSerializer(user)
    #     return Response(serializer.data)

    # def create(self, request, *args, **kwargs):
    #     """
    #     Checks if post request data is an array initializes serializer with many=True else executes
    #     default CreateModelMixin.create function
    #     """
    #     if not isinstance(request.data, list):
    #         return super(FarmerViewSet, self).create(request, *args, **kwargs)
    #     else:
    #         serializer = self.get_serializer(data=request.data, many=True)
    #         serializer.is_valid(raise_exception=True)
    #         self.perform_create(serializer)
    #         headers = self.get_success_headers(serializer.data)
    #         return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
