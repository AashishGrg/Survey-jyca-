from django.urls import path

from .views import FarmerCreateView

urlpatterns = [
    path('create/', FarmerCreateView.as_view(), name='farmer_crop_create'),
]
