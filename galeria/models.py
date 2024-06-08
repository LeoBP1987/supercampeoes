from django.db import models
from datetime import datetime
from usuarios.models import UsuariosCustomizados

class Times(models.Model):
    nome_curto = models.CharField(max_length=50, null=False, blank=False)
    nome_completo = models.CharField(max_length=100, null=False, blank=False)
    estado = models.CharField(max_length=50, null=False, blank=False)
    simbolo = models.ImageField(upload_to='simbolo/%Y/%m/%d', blank=False)
    historico = models.TextField(null=False, blank=False)
    publicado = models.BooleanField(default=True)
    data_registro = models.DateField(default=datetime.now, blank=False)
    usuario = models.ForeignKey(
        to=UsuariosCustomizados,
        on_delete=models.SET_NULL,
        null=True,
        blank=False,
        related_name='user'
    )

    def __str__(self):
        return self.nome_curto