"""Leg serializers """

# Django REST Framework
from rest_framework import serializers
# Models
from auxo_assesment.flights.models import Leg


class LegModelSerializer(serializers.ModelSerializer):
    """ Leg model serializers """

    departure_airport = serializers.SlugRelatedField(
        many=False, read_only=True, slug_field='code'
    )
    arrival_airport = serializers.SlugRelatedField(
        many=False, read_only=True, slug_field='code'
    )

    airline_name = serializers.StringRelatedField(
        many=False, read_only=True, source='airline')

    airline_id = serializers.PrimaryKeyRelatedField(
        many=False, read_only=True, source='airline')

    class Meta:
        model = Leg
        fields = (
            'id',
            'leg_id',
            'stops',
            'duration_mins',
            'arrival_airport',
            'departure_airport',
            'airline_id',
            'airline_name',
            'departure_time',
            'arrival_time'
        )
