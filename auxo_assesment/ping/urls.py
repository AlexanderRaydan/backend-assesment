# Django
from django.urls import path

# Ping Views
from auxo_assesment.ping.views import PingAPIView

urlpatterns = [
    path('ping/', PingAPIView.as_view(), name='ping'),
]
