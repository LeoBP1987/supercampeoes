from django import forms
from galeria.models import Times, DeclararCampeao

class TimeForms(forms.ModelForm):
    class Meta:
        model = Times
        exclude = ['publicado', 'data_registro', 'usuario']
        fields = ['nome_curto', 'nome_completo', 'estado', 'simbolo', 'historico']
        widgets = {
            'nome_curto': forms.TextInput(attrs={'class':'cadastro__input'}),
            'nome_completo': forms.TextInput(attrs={'class':'cadastro__input'}),
            'estado': forms.TextInput(attrs={'class':'cadastro__input'}),
            'simbolo':forms.FileInput(attrs={'class':'cadastro__input'}),
            'historico': forms.Textarea(attrs={'class':'cadastro__input'}),
        }

class CampeoesForms(forms.ModelForm):
    class Meta:
        model = DeclararCampeao
        exclude = ['time', 'pontuacao',]
        labels = {
            'campeonato': 'Campeonato que o time conquistou',
            'quantidade': 'Quantidade de vezes que foi conquistado'
        }
        widgets = {
            'campeonato': forms.Select(attrs={'class':'cadastro__input'}),
            'quantidade': forms.TextInput(attrs={'class':'cadastro__input'})
        }