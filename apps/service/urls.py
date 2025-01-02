from django.urls import path

from .views import (
    ServiceListView,
    ServiceDetailView
)

urlpatterns = [
    path('services/', ServiceListView.as_view(), name='services'),
    path('services/<slug:slug>/', ServiceDetailView.as_view(), name='service-detail')
]