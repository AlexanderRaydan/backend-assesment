""" Leg models """
# Django
from django.db import models

# Models
from auxo_assesment.flights.models import FlightsBaseModel


class Leg(FlightsBaseModel, models.Model):
    """ legs model """

    # Relations
    departure_airport = models.ForeignKey(
        'flights.Airport', on_delete=models.PROTECT, related_name='%(class)s_departure_airport')
    arrival_airport = models.ForeignKey(
        'flights.Airport', on_delete=models.PROTECT, related_name='%(class)s_arrival_airport')
    airline = models.ForeignKey(
        'flights.Airline', on_delete=models.PROTECT, related_name='legs')
    itineraries = models.ManyToManyField(
        'flights.Itinerary', related_name='legs',)

    # Id
    leg_id = models.CharField(unique=True, null=False, max_length=20)

    # Date fields
    departure_time = models.DateTimeField(null=False)
    arrival_time = models.DateTimeField(null=False)

    # Data
    duration_mins = models.IntegerField(null=False,)
    stops = models.IntegerField(null=False, default=0)

    def __str__(self):
        """ Return leg """
        return f" Airline: {self.airline.name} from {self.departure_airport.name} to {self.arrival_airport.name}"

    REQUIRED_FIELDS = ['departure_airport', 'arrival_airport',
                       'airline', 'departure_time', 'arrival_time', 'duration', 'stops']
