from django.contrib.auth.models import AbstractUser
from django.db import models

class UsuariosCustomizados(AbstractUser):
    nome_completo=models.CharField(max_length=150, null=False, blank=False)
    time=models.CharField(max_length=50)

    def __str__(self):
        return self.username
