# Django
from django.urls import path

# Ping Views
from auxo_assesment.flights.views import ItinerariesAPIView

urlpatterns = [
    path('itineraries/', ItinerariesAPIView.as_view(), name='itineraries'),
]
