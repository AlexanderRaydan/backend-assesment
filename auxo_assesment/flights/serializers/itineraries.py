# Django REST Framework
from rest_framework import serializers
# Models
from auxo_assesment.flights.models import Itinerary


class ItineraryModelSerializer(serializers.ModelSerializer):
    """ Itinerary model serializers """

    agent_rating = serializers.SlugRelatedField(
        many=False, read_only=True, source='agent', slug_field='rating')

    agent = serializers.SlugRelatedField(
        many=False, read_only=True, slug_field='name')

    class Meta:
        model = Itinerary
        fields = ('id', 'itinerary_id', 'legs',
                  'price', 'agent_rating', 'agent')
