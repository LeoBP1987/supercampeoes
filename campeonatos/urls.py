from django.urls import path
from campeonatos.views import Campeonatos

urlpatterns = [
    path('campeonatos/', Campeonatos, name='campeonatos'),
]