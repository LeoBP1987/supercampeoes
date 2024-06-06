from django.contrib import admin
from usuarios.models import UsuariosCustomizados

class ListandoUsuarios(admin.ModelAdmin):
    list_display=('id', 'nome_completo', 'username', 'time', 'is_active')
    list_display_links=('id', 'username')
    search_fields=('id', 'username', 'time')
    list_filter=('time',)
    list_per_page=10

admin.site.register(UsuariosCustomizados, ListandoUsuarios)