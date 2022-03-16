""" Itinerary Model Test. """

#  Django
from django.test import TestCase

# Models
from auxo_assesment.flights.models import Itinerary

# test Utils
from auxo_assesment.flights.tests.utils import *


class ItineraryTestCase(TestCase):
    """ Itinerary test class """

    def setUp(self):
        self.airline = create_airline()
        self.agent = create_agent()
        self.itinerary = create_itinerary(agent=self.agent)

    def test_itinerary_success(self):
        """ itinerary success """
        itinerary = Itinerary.objects.get(pk=self.itinerary.id,)
        self.assertEqual(itinerary.name, ITINERARY_NAME_TEST)

        self.assertEqual(itinerary.agent.id, self.agent.id)
        self.assertEqual(itinerary.price, ITINERARY_PRICE_TEST)

        self.assertEqual(itinerary.is_active, True)
