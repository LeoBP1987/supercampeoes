from typing import Any
from django import forms
from campeonatos.models import Campeonato



class CampeonatoForms(forms.ModelForm):
    class Meta:
        model = Campeonato
        exclude=['pontuacao','data_registro', 'usuario', 'ativo',]
        labels = {
            'nome_campeonato':'Nome do Campeonato',
            'categoria':'Categoria',
            'principal':'Principal titulo da categoria?'
        }
        widgets = {
            'nome_campeonato':forms.TextInput(attrs={'class':'cadastro__input',}),
            'categoria':forms.Select(attrs={'class':'cadastro__input',}),
            'principal':forms.Select(attrs={'class':'cadastro__input',}),
        }