from django.db import models
from datetime import datetime
from usuarios.models import UsuariosCustomizados

class Categoria(models.Model):
    categoria = models.CharField(max_length=100, null=False, blank=False)
    pontuacao = models.IntegerField(null=False, blank=False)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.categoria
    
class Campeonato(models.Model):

    OPCOES_PRINCIPAL = [
        ("SIM","Sim"),
        ("NÃO","Não"),
    ]

    nome_campeonato = models.CharField(max_length=100, null=False, blank=False)

    categoria = models.ForeignKey(
        to=Categoria, 
        on_delete=models.SET_NULL,
        null=True,
        blank=False,
        related_name='cat')
    
    principal = models.CharField(max_length=5, choices=OPCOES_PRINCIPAL, default='')

    pontuacao = models.IntegerField(null=False, blank=False)

    data_registro = models.DateTimeField(default=datetime.now, blank=False)

    usuario = models.ForeignKey(
        to=UsuariosCustomizados, 
        on_delete=models.SET_NULL,
        null=True,
        blank=False,
        related_name='usuario')
    
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.nome_campeonato