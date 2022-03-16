# Django
from django.contrib import admin

# Models
from auxo_assesment.flights.models import *


@admin.register(Airport)
class AirportAdmin(admin.ModelAdmin):
    """ Airport model admin """
    list_display = ('name', 'code', 'is_active')
    search_fields = ('name', 'code')
    list_filter = ('is_active',)


@admin.register(Airline)
class AirlineAdmin(admin.ModelAdmin):
    """ Airline model admin """
    list_display = ('name', 'is_active')
    search_fields = ('name',)
    list_filter = ('is_active',)


@admin.register(Leg)
class LegAdmin(admin.ModelAdmin):
    """ Leg model admin """
    list_display = ('name', 'departure_airport',
                    'arrival_airport', 'is_active')
    search_fields = ('arrival_airport__name', 'departure_airport__name')
    list_filter = ('departure_time', 'arrival_time',
                   'duration_mins', 'stops', 'airline', 'is_active')


@admin.register(Agent)
class AgentAdmin(admin.ModelAdmin):
    """ Agent model admin """
    list_display = ('name', 'rating', 'is_active')
    search_fields = ('name',)
    list_filter = ('rating', 'is_active')


@admin.register(Itinerary)
class ItineraryAdmin(admin.ModelAdmin):
    """ Itinerary model admin """
    list_display = ('name', 'price', 'agent', 'is_active')
    search_fields = ('name',)
    list_filter = ('price', 'agent__rating', 'is_active')
