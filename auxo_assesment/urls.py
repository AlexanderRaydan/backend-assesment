"""auxo_assesment URL Configuration"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(('auxo_assesment.ping.urls', 'ping'), namespace='ping')),
    path('flights/', include(('auxo_assesment.flights.urls',
         'flights'), namespace='flights')),
]
