from django.urls import path

from .views import (
    ServiceDetailView,
    ServiceListView,
)

urlpatterns = [
    path(
        "services/",
        ServiceListView.as_view(),
        name="services",
    ),
    path(
        "services/<slug:slug>/",
        ServiceDetailView.as_view(),
        name="service-detail",
    ),
]
