""" Utils """

from auxo_assesment.flights.models import *

json = {
    "itineraries": [
        {
            "id": "it_1",
            "legs": [
                  "leg_1",
                "leg_4"
            ],
            "price": 35,
            "agent": "Wizzair.com",
            "agent_rating": 9.1
        },
        {
            "id": "it_2",
            "legs": [
                "leg_2",
                "leg_5"
            ],
            "price": 115,
            "agent": "British Airways",
            "agent_rating": 9.3
        },
        {
            "id": "it_3",
            "legs": [
                "leg_3",
                "leg_6"
            ],
            "price": 90,
            "agent": "Lufthansa",
            "agent_rating": 8.9
        },
        {
            "id": "it_4",
            "legs": [
                "leg_1",
                "leg_5"
            ],
            "price": 105,
            "agent": "Trip.com",
            "agent_rating": 9.5
        },
        {
            "id": "it_5",
            "legs": [
                "leg_1",
                "leg_6"
            ],
            "price": 195,
            "agent": "Trip.com",
            "agent_rating": 9.5
        },
        {
            "id": "it_6",
            "legs": [
                "leg_2",
                "leg_4"
            ],
            "price": 93,
            "agent": "Kiwi.com",
            "agent_rating": 8.0
        },
        {
            "id": "it_7",
            "legs": [
                "leg_3",
                "leg_4"
            ],
            "price": 42,
            "agent": "CheapFligths",
            "agent_rating": 10.0
        }
    ],
    "legs": [
        {
            "id": "leg_1",
            "departure_airport": "BUD",
            "arrival_airport": "LTN",
            "departure_time": "2020-10-31T15:35",
            "arrival_time": "2020-10-31T17:00",
            "stops": 0,
            "airline_name": "Wizz Air",
            "airline_id": "WZ",
            "duration_mins": 145
        },
        {
            "id": "leg_2",
            "departure_airport": "BUD",
            "arrival_airport": "LHR",
            "departure_time": "2020-10-31T12:05",
            "arrival_time": "2020-10-31T17:00",
            "stops": 1,
            "airline_name": "British Airways",
            "airline_id": "BA",
            "duration_mins": 190
        },
        {
            "id": "leg_3",
            "departure_airport": "BUD",
            "arrival_airport": "LGW",
            "departure_time": "2020-10-31T22:35",
            "arrival_time": "2020-11-01T00:10",
            "stops": 0,
            "airline_name": "Lufthansa",
            "airline_id": "LH",
            "duration_mins": 155
        },
        {
            "id": "leg_4",
            "departure_airport": "LTN",
            "arrival_airport": "BUD",
            "departure_time": "2020-11-11T19:45",
            "arrival_time": "2020-11-11T21:10",
            "stops": 0,
            "airline_name": "Wizz Air",
            "airline_id": "WZ",
            "duration_mins": 145
        },
        {
            "id": "leg_5",
            "departure_airport": "LHR",
            "arrival_airport": "BUD",
            "departure_time": "2020-11-11T11:25",
            "arrival_time": "2020-11-11T19:10",
            "stops": 1,
            "airline_name": "British Airways",
            "airline_id": "BA",
            "duration_mins": 190
        },
        {
            "id": "leg_6",
            "departure_airport": "LGW",
            "arrival_airport": "BUD",
            "departure_time": "2020-11-11T08:10",
            "arrival_time": "2020-11-11T11:40",
            "stops": 0,
            "airline_name": "Lufthansa",
            "airline_id": "LH",
            "duration_mins": 150
        }
    ]
}


def load_data_from_json():

    raw_itineraries = json['itineraries']
    raw_legs = json['legs']

    # Get airport

    airports_codes = [d['arrival_airport'] for d in raw_legs if 'arrival_airport' in d] + \
        [d['arrival_airport'] for d in raw_legs if 'arrival_airport' in d]

    airports_codes = list(set(airports_codes))

    for code in airports_codes:
        Airport.objects.create(
            name=code,
            code=code
        )

    # Get airline name and id
    airlines_names = [(d['airline_name'], d['airline_id'])
                      for d in raw_legs if 'airline_name' in d and 'airline_id' in d]

    airlines_names = list(set(airlines_names))

    for info in airlines_names:

        Airline.objects.create(
            name=info[0],
            airline_id=info[1]
        )

    # Get agent name and rating
    agent_names = [(d['agent'], d['agent_rating'])
                   for d in raw_itineraries if 'agent' in d and 'agent_rating' in d]

    agent_names = list(set(agent_names))

    for info in agent_names:

        Agent.objects.create(
            name=info[0],
            rating=info[1]
        )

    # create Itineraries
    for itinerary in raw_itineraries:

        agent = Agent.objects.get(name=itinerary['agent'])
        itinerary_id = itinerary['id']
        price = itinerary['price']
        Itinerary.objects.create(
            name=itinerary_id, itinerary_id=itinerary_id, agent=agent, price=price)

    # Get itinerary Id foreach leg
    itineraries_ids_by_leg = {}

    for itinerary in raw_itineraries:
        itinerary_id = itinerary['id']
        legs = itinerary['legs']

        for leg in legs:

            pre_itineraries_ids = []

            # Verify if exist key and save previous itineraries_ids
            if leg in itineraries_ids_by_leg.keys():
                pre_itineraries_ids = itineraries_ids_by_leg[leg]

            pre_itineraries_ids.append(itinerary_id)
            itineraries_ids_by_leg[leg] = pre_itineraries_ids

    # create Legs
    for leg in raw_legs:

        # departure_airport = Airport.objects.get(name=itinerary['name'])
        leg_id = leg['id']
        departure_airport_name = leg['departure_airport']
        arrival_airport_name = leg['arrival_airport']
        airline_id = leg['airline_id']

        departure_time = leg['departure_time']
        arrival_time = leg['arrival_time']
        stops = leg['stops']
        duration_mins = leg['duration_mins']

        # Get airport

        departure_airport = Airport.objects.get(name=departure_airport_name)
        arrival_airport = Airport.objects.get(name=arrival_airport_name)
        airline = Airline.objects.get(airline_id=airline_id)

        # Get itinerary

        itineraries_ids = itineraries_ids_by_leg[leg_id]
        leg_itineraries = Itinerary.objects.filter(
            itinerary_id__in=itineraries_ids)

        leg = Leg.objects.create(
            leg_id=leg_id,
            name=leg_id,
            departure_time=departure_time,
            arrival_time=arrival_time,
            stops=stops,
            duration_mins=duration_mins,
            departure_airport=departure_airport,
            arrival_airport=arrival_airport,
            airline=airline,
        )

        leg.itineraries.set(leg_itineraries)


load_data_from_json()

print('DATA CREATED !')
