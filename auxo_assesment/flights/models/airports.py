""" Airports models """
# Django
from django.db import models

# Models
from auxo_assesment.flights.models import FlightsBaseModel


class Airport(FlightsBaseModel, models.Model):
    """ Airports model """
    code = models.CharField(max_length=4, null=False, unique=True,)

    def __str__(self):
        """ Return airport name """
        return str(self.name)

    REQUIRED_FIELDS = ['code', ]
