""" Airline models """
# Django
from django.db import models

# Models
from auxo_assesment.flights.models.flights_base_models import FlightsBaseModel


class Airline(FlightsBaseModel, models.Model):
    """ Airlines model """

    airline_id = models.CharField(unique=True, null=False, max_length=20)

    def __str__(self):
        """ Return airline name """
        return str(self.name)
