from django.contrib import admin
from galeria.models import Times, DeclararCampeao

class ListandoTimes(admin.ModelAdmin):
    list_display = ('id', 'nome_curto', 'estado',)
    list_display_links = ('id', 'nome_curto',)
    search_fields = ('nome_curto', 'nome_completo', 'estado')
    list_filter = ('estado',)
    list_per_page = 10

class ListandoCampeoes(admin.ModelAdmin):
    list_display = ('id', 'time', 'campeonato', 'quantidade', 'pontuacao')
    list_display_links = ('id', 'time')
    list_per_page = 10

admin.site.register(Times, ListandoTimes)
admin.site.register(DeclararCampeao, ListandoCampeoes)