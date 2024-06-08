from django.contrib import admin
from campeonatos.models import Categoria, Campeonato

class ListandoCategorias(admin.ModelAdmin):
    list_display=('id', 'categoria', 'pontuacao', 'ativo')
    list_display_links=('id', 'categoria')
    search_fields=('categoria',)
    list_per_page=10

class ListandoCampeonatos(admin.ModelAdmin):
    list_display=('id', 'nome_campeonato', 'categoria', 'pontuacao', 'ativo')
    list_display_links=('id', 'nome_campeonato', 'categoria', 'ativo')
    search_fields=('categoria',)
    list_filter=('categoria',)
    list_per_page=10

admin.site.register(Categoria, ListandoCategorias)
admin.site.register(Campeonato, ListandoCampeonatos)
