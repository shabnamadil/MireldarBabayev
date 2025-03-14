from django.urls import path

from .views import AppointmentPostAPIView

urlpatterns = [path('appointment/', AppointmentPostAPIView.as_view())]
