""" Flights Base Model """
# Django
from django.db import models

# Models
from auxo_assesment.models import AuxoAssesmentModel


class FlightsBaseModel(AuxoAssesmentModel, models.Model):
    """ Flights Base Model """
    name = models.CharField(max_length=100, null=False, unique=True,)
    is_active = models.BooleanField(default=True, null=False)

    REQUIRED_FIELDS = ['name', ]

    class Meta:
        """meta options"""
        abstract = True
        get_latest_by = 'created_at'
        ordering = ['-created_at', '-updated_at']
