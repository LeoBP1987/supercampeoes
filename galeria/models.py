from django.db import models
from datetime import datetime
from usuarios.models import UsuariosCustomizados

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

    def __str__(self):
        return self.nome_curto