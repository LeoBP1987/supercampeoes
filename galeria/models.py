from django.db import models
from datetime import datetime
from usuarios.models import UsuariosCustomizados
from campeonatos.models import Campeonato

class Times(models.Model):
    nome_curto = models.CharField(max_length=50, null=False, blank=False)
    nome_completo = models.CharField(max_length=100, null=False, blank=False)
    estado = models.CharField(max_length=50, null=False, blank=False)
    simbolo = models.ImageField(upload_to='simbolo/%Y/%m/%d', blank=True)
    historico = models.TextField(null=False, blank=False)
    publicado = models.BooleanField(default=True)
    data_registro = models.DateTimeField(default=datetime.now)
    usuario = models.ForeignKey(
        to=UsuariosCustomizados,
        on_delete=models.SET_NULL,
        null=True,
        related_name='usu'
    )
    titulos = models.ManyToManyField(
        to=Campeonato,
        through='DeclararCampeao'
    )
    foto_mascote = models.ImageField(upload_to='mascote/%Y/%m/%d', blank=True)
    nome_mascote = models.CharField(max_length=50, blank=True)
    descricao_mascote = models.TextField(blank=True)

    def __str__(self):
        return self.nome_curto    
    
class DeclararCampeao(models.Model):
    time = models.ForeignKey(
        to=Times,
        on_delete=models.CASCADE,
    )

    campeonato = models.ForeignKey(
        to=Campeonato,
        on_delete=models.CASCADE,
    )

    quantidade = models.IntegerField(default=0)

    pontuacao = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.time.nome_curto} ganhou {self.campeonato.nome_campeonato} {self.quantidade} vezes'