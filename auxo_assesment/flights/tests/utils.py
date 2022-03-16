# Datetime
from datetime import datetime

# Models
from auxo_assesment.flights.models import *

AIRPORT_NAME_TEST = 'Manaos Airport'

AIRLINE_NAME_TEST = 'Manaos Airline'
AGENT_NAME_TEST = 'Manaos Agent'
AGENT_RATING_TEST = 8.0
ITINERARY_NAME_TEST = 'Manaos Itinerary'
ITINERARY_PRICE_TEST = 80000

LEG_NAME_TEST = 'Manaos Leg'

LEG_DURATION_TEST = 200
LEG_STOPS_TEST = 0


def create_airport(code, name=AIRPORT_NAME_TEST):
    airport = Airport.objects.create(name=name, code=code)
    return airport


def create_airline(airline_id='MM', name=AIRLINE_NAME_TEST):
    airline = Airline.objects.create(name=name, airline_id=airline_id)
    return airline


def create_agent(name=AGENT_NAME_TEST, rating=AGENT_RATING_TEST):

    agent = Agent.objects.create(
        name=name, rating=rating)

    return agent


def create_itinerary(agent, name=ITINERARY_NAME_TEST, price=ITINERARY_PRICE_TEST, itinerary_id='it_1'):

    itinerary = Itinerary.objects.create(price=price, agent=agent, name=name)

    return itinerary


def create_leg(
    departure_airport,
    arrival_airport,
    itineraries,
    airline,
    departure_time=datetime.now(),
    arrival_time=datetime.now(),
    stops=LEG_STOPS_TEST,
    duration_mins=LEG_DURATION_TEST,
    name=LEG_NAME_TEST,
    leg_id='leg_1'
):

    leg = Leg.objects.create(
        departure_airport=departure_airport,
        arrival_airport=arrival_airport,
        departure_time=departure_time,
        arrival_time=arrival_time,
        airline=airline,
        stops=stops,
        duration_mins=duration_mins,
        name=name,
        leg_id=leg_id
    )

    leg.itineraries.set(itineraries)
    return leg
