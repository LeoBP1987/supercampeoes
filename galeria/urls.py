from django.urls import path
from galeria.views import index, times, ranking, meus_times, novo_time, \
      editar_time, deletar_time, ranking_geral, titulos, novo_titulo, editar_titulo, \
      deletar_titulo

urlpatterns = [
    path('', index, name='index'),
    path('times/<int:time_id>', times, name='times'),
    path('ranking/', ranking, name='ranking'),
    path('meus_times/', meus_times, name='meus_times'),
    path('novo_time/', novo_time, name='novo_time'),
    path('editar_time/<int:time_id>', editar_time, name='editar_time'),
    path('deletar_time/<int:time_id>', deletar_time, name='deletar_time'),
    path('ranking_geral/', ranking_geral, name='ranking_geral'),
    path('titulos/<int:time_id>', titulos, name='titulos'),
    path('novo_titulo/<int:time_id>', novo_titulo, name='novo_titulo'),
    path('editar_titulo/<int:titulo_id>', editar_titulo, name='editar_titulo'),
    path('deletar_titulo/<int:titulo_id>', deletar_titulo, name='deletar_titulo'),
]