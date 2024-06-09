from django.urls import path
from campeonatos.views import campeonatos, novo_campeonato, editar_campeonato, deletar_campeonato

urlpatterns = [
    path('campeonatos/', campeonatos, name='campeonatos'),
    path('novo_campeonato/', novo_campeonato, name='novo_campeonato'),
    path('editar_campeonato/<int:campeonato_id>', editar_campeonato, name='editar_campeonato'),
    path('deletar_campeonato/<int:campeonato_id>', deletar_campeonato, name='deletar_campeonato'),
]