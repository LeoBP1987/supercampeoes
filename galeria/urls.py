from django.urls import path
from galeria.views import index, times, ranking, meus_times, novo_time

urlpatterns = [
    path('', index, name='index'),
    path('times/<int:time_id>', times, name='times'),
    path('ranking/', ranking, name='ranking'),
    path('meus_times/', meus_times, name='meus_times'),
    path('novo_time/', novo_time, name='novo_time')
]