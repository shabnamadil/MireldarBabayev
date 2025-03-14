from django.urls import path

from .views import AppointmentPageView

urlpatterns = [
    path('appointment/', AppointmentPageView.as_view(), name='appointment')
]
