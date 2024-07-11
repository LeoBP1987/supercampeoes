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

def listar_campeonatos():

    campeonatos = Campeonato.objects.all()

    lista_campeonatos = []

    for campeonato in campeonatos:
        if (campeonato.nome_campeonato, campeonato.nome_campeonato) not in lista_campeonatos:
            lista_campeonatos.append((campeonato.nome_campeonato, campeonato.nome_campeonato))

    return lista_campeonatos

lista_campeonatos = listar_campeonatos()

class RkCampeonatosForms(forms.Form):
    campeonato = forms.ChoiceField(choices=lista_campeonatos, widget=forms.Select(attrs={'class':'cadastro__input',}), label='Escolha o Campeonato que pretende Rankear')
