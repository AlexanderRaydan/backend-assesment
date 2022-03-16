""" Agents models """
# Django
from django.db import models

# Models
from auxo_assesment.flights.models import FlightsBaseModel


class Agent(FlightsBaseModel, models.Model):
    """ Agents model """

    # Stats
    rating = models.FloatField(null=False, default=0.0)

    def __str__(self):
        """ Return agent name """
        return str(self.name)

    REQUIRED_FIELDS = ['airline', ]
