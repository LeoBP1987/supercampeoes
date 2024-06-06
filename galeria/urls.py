from django.urls import path
from galeria.views import index, times, ranking

urlpatterns = [
    path('', index, name='index'),
    path('times/', times, name='times'),
    path('ranking/', ranking, name='ranking'),
]