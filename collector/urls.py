from django.urls import path

from .views import CollectorGroupAPIView

urlpatterns = [
    path('list/', CollectorGroupAPIView.as_view(), name='collector_list'),
]
