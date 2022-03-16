""" Agent Model Test. """

#  Django
from django.test import TestCase

# Models
from auxo_assesment.flights.models import Agent

# test Utils
from auxo_assesment.flights.tests.utils import create_agent, create_airline


class AgentTestCase(TestCase):
    """ Agent test class """

    def setUp(self):
        self.airline = create_airline(name='Manaos Airline',)
        create_agent(name='Manaos agent')

    def test_agent_success(self):
        """ agent success """
        agent = Agent.objects.get(name='Manaos agent',)
        self.assertEqual(agent.name, 'Manaos agent')
        self.assertEqual(agent.rating, 8.0)

        self.assertEqual(agent.is_active, True)
