""" Itinerary models """
# Django
from django.db import models

# Models
from auxo_assesment.flights.models import FlightsBaseModel


class Itinerary(FlightsBaseModel, models.Model):
    """ Itinerary model """

    # Relations
    agent = models.ForeignKey(
        'flights.Agent', on_delete=models.PROTECT, related_name='agent')

    itinerary_id = models.CharField(unique=True, null=False, max_length=20)

    # Data
    price = models.FloatField(null=False, default=0.0)

    def __str__(self):
        """ Return itinerary name """
        return str(self.name)

    REQUIRED_FIELDS = ['agent', 'price']
