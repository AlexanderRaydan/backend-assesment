""" Leg Model Test. """

#  Django
from django.test import TestCase

# Models
from auxo_assesment.flights.models import Leg

# test Utils
from auxo_assesment.flights.tests.utils import *


class LegTestCase(TestCase):
    """ Leg test class """

    def setUp(self):

        self.arrival_airport = create_airport(code='AD', name='Manaos')
        self.departure_airport = create_airport(code='AP', name='Rio')

        self.airline = create_airline()
        self.agent = create_agent()

        self.itinerary = create_itinerary(agent=self.agent)

        self.leg = create_leg(
            arrival_airport=self.arrival_airport,
            departure_airport=self.departure_airport,
            airline=self.airline,
            itineraries=[self.itinerary])

    def test_leg_success(self):
        """ leg success """
        leg = Leg.objects.get(pk=self.leg.id,)
        self.assertEqual(leg.name, LEG_NAME_TEST)
        self.assertEqual(leg.duration_mins, LEG_DURATION_TEST)
        self.assertEqual(leg.stops, LEG_STOPS_TEST)
        self.assertEqual(leg.arrival_airport.id, self.arrival_airport.id)
        self.assertEqual(leg.departure_airport.id, self.departure_airport.id)
        self.assertEqual(leg.airline.id, self.airline.id)
        self.assertEqual(leg.is_active, True)
