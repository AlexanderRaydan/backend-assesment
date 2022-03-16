""" Ping test !"""

#  Django REST Framework
from rest_framework import status
from rest_framework.test import APITestCase


# Test Utils
from auxo_assesment.flights.tests.utils import *

URL = '/flights/itineraries/'


class ItineraryAPITestCase(APITestCase):
    """ Itineraries test class """

    def setUp(self):
        self.arrival_airport_test = create_airport(code='AD', name='Manaos')
        self.departure_airport_test = create_airport(code='AP', name='Rio')

        self.airline_test = create_airline()
        self.agent_test = create_agent()
        self.itinerary_test = create_itinerary(agent=self.agent_test)

        self.leg_test = create_leg(
            arrival_airport=self.arrival_airport_test,
            departure_airport=self.departure_airport_test,
            airline=self.airline_test,
            itineraries=[self.itinerary_test])

    def test_get_itineraries_success(self):
        """ Itineraries success """

        response = self.client.get(path=URL, format='json')
        self.assertEqual(response.status_code, 200)

        body = response.data

        # Validate Body
        self.assertEqual(len(body), 2)

        self.assertEqual(len(body['legs']), 1)
        self.assertEqual(len(body['itineraries']), 1)

        # Validate legs
        leg = body['legs'][0]

        self.assertEqual(leg['id'], self.leg_test.id)
        self.assertEqual(leg['departure_airport'],
                         self.departure_airport_test.code)
        self.assertEqual(leg['arrival_airport'],
                         self.arrival_airport_test.code)
        self.assertEqual(leg['stops'], self.leg_test.stops)
        self.assertEqual(leg['airline_name'], self.airline_test.name)
        self.assertEqual(leg['airline_id'], self.airline_test.id)
        self.assertEqual(leg['duration_mins'], self.leg_test.duration_mins)

        # Validate Itineraries
        itinerary = body['itineraries'][0]

        self.assertEqual(itinerary['id'], self.itinerary_test.id)
        self.assertEqual(itinerary['price'],
                         self.itinerary_test.price)
        self.assertEqual(itinerary['agent'],
                         self.itinerary_test.agent.name)
        self.assertEqual(itinerary['agent_rating'],
                         self.itinerary_test.agent.rating)
        self.assertEqual(len(itinerary['legs']), 1)
        self.assertEqual(itinerary['legs'][0], self.leg_test.id)

    def test_get_itineraries_filters(self):
        """ Itineraries success """

        response = self.client.get(
            path=f'{URL}?stops=100&price=200000', format='json')
        self.assertEqual(response.status_code, 200)

        body = response.data

        # Validate Body
        self.assertEqual(len(body), 2)

        self.assertEqual(len(body['legs']), 0)
        self.assertEqual(len(body['itineraries']), 0)
