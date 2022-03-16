""" Airport Model Test. """

#  Django
from django.test import TestCase

# Models
from auxo_assesment.flights.models import Airport

# test Utils
from auxo_assesment.flights.tests.utils import create_airport


class AirportTestCase(TestCase):
    """ Airport test class """

    def setUp(self):
        create_airport(name='Manaos Airport', code='MANA')

    def test_airport_success(self):
        """ airport success """
        airport = Airport.objects.get(code='MANA')
        self.assertEqual(airport.name, 'Manaos Airport')
        self.assertEqual(airport.code, 'MANA')
        self.assertEqual(airport.is_active, True)
