""" Airline Model Test. """

#  Django
from django.test import TestCase

# Models
from auxo_assesment.flights.models import Airline

# test Utils
from auxo_assesment.flights.tests.utils import create_airline


class AirlineTestCase(TestCase):
    """ Airline test class """

    def setUp(self):
        create_airline(name='Manaos Airline',)

    def test_bank_success(self):
        """ Airline success """
        airline = Airline.objects.get(name='Manaos Airline')
        self.assertEqual(airline.name, 'Manaos Airline')
        self.assertEqual(airline.is_active, True)
