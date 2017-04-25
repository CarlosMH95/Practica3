from django.conf.urls import url, include
from Persona.views import persona

urlpatterns = [
    url(r'^(?P<id>\d+)/',persona)
]