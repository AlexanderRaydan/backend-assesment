

""" Itineraries views. """

# Django REST Framework
from rest_framework.views import APIView
from rest_framework.response import Response

# Serializers
from auxo_assesment.flights.serializers import LegModelSerializer, ItineraryModelSerializer

# Models
from auxo_assesment.flights.models import Leg, Itinerary


class ItinerariesAPIView(APIView):
    def get(self, request, *args, **kwargs):

        # Filter
        stops = request.GET.get('stops')
        price = request.GET.get('price')

        # Itineraries
        itineraries = Itinerary.objects.all()
        if price is not None:
            itineraries = itineraries.filter(price=price)

        itineraries_serializer = ItineraryModelSerializer(
            itineraries, many=True)

        # Legs
        legs = Leg.objects.all()
        if stops is not None:
            legs = legs.filter(stops=stops)

        legs_serializer = LegModelSerializer(legs, many=True)

        response = {
            'itineraries': itineraries_serializer.data,
            'legs': legs_serializer.data,
        }

        return Response(response)
