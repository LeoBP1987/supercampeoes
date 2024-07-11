from django import forms
from galeria.models import Times, DeclararCampeao

class TimeForms(forms.ModelForm):
    class Meta:
        model = Times
        exclude = ['publicado', 'data_registro', 'usuario']
        fields = ['nome_curto', 'nome_completo', 'estado', 'simbolo', 'historico', 'foto_mascote', 'nome_mascote', 'descricao_mascote']
        widgets = {
            'nome_curto': forms.TextInput(attrs={'class':'cadastro__input'}),
            'nome_completo': forms.TextInput(attrs={'class':'cadastro__input'}),
            'estado': forms.TextInput(attrs={'class':'cadastro__input'}),
            'simbolo':forms.FileInput(attrs={'class':'cadastro__input'}),
            'historico': forms.Textarea(attrs={'class':'cadastro__input'}),
            'foto_mascote': forms.FileInput(attrs={'class':'cadastro__input'}),
            'nome_mascote': forms.TextInput(attrs={'class':'cadastro__input'}),
            'descricao_mascote': forms.Textarea(attrs={'class':'cadastro__input'})
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

def listar_estados():
    times = Times.objects.all()

    estados = []

    for time in times:
        if (time.estado, time.estado) not in estados:
            estados.append((time.estado, time.estado))

    return estados

estados = listar_estados()

class EstadoForms(forms.Form):
    estado = forms.ChoiceField(choices=estados, label='Selecione o Estado que deseja Rankear', widget=forms.Select(attrs={'class':'cadastro__input'}))