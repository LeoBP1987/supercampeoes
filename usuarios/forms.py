from typing import Any
from django import forms
from usuarios.models import UsuariosCustomizados

class LoginForms(forms.Form):
    login=forms.CharField(
        label='Login',
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class':'cadastro__input',
                'placeholder':'Digite aqui o seu login'
            },
        ),
    )

    senha=forms.CharField(
        label='Senha',
        required=True,
        max_length=100,
        widget=forms.PasswordInput(
            attrs={
                'class':'cadastro__input',
                'placeholder':'Digite aqui sua senha'
            }
        )
    )

class CadastroForms(forms.Form):
    nome_completo = forms.CharField(
        label='Nome Completo',
        required=True,
        max_length=150,
        widget=forms.TextInput(
            attrs={
                'class':'cadastro__input',
                'placeholder':'Ex.: João Silva'
            }
        )
    )

    email = forms.EmailField(
        label='Email',
        required=True,
        max_length=100,
        widget=forms.EmailInput(
            attrs={
                'class':'cadastro__input',
                'placeholder':'Ex.: joaosilva@email.com'
            }
        )
    )

    time = forms.CharField(
        label='Time do Coração',
        required=True,
        max_length=50,
        widget=forms.TextInput(
            attrs={
                'class':'cadastro__input',
                'placeholder':'Digite seu time do coração'
            }
        )
    )

    login = forms.CharField(
        label='Login',
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class':'cadastro__input',
                'placeholder':'Ex.: joao_silva'
            }
        )
    )

    senha = forms.CharField(
        label='Senha',
        required=True,
        max_length=100,
        widget=forms.PasswordInput(
            attrs={
                'class':'cadastro__input',
                'placeholder':'Digite uma senha'
            }
        )
    )

    confirma_senha = forms.CharField(
        label='Confirmar Senha',
        required=True,
        max_length=100,
        widget=forms.PasswordInput(
            attrs={
                'class':'cadastro__input',
                'placeholder':'Confirme a senha escolhida'
            }
        )
    )

    def clean_login(self):        
        nome = self.cleaned_data.get('login')

        if nome:
            nome = nome.strip()
            if ' ' in nome:
                raise forms.ValidationError('Espaços não são permitidos nos logins')
            else:
                if UsuariosCustomizados.objects.filter(username=nome).exists():
                    raise forms.ValidationError('Este Login já está em uso.')
                else:
                    return nome
            
    def clean_confirma_senha(self):
        senha = self.cleaned_data.get('senha')
        confirma_senha = self.cleaned_data.get('confirma_senha')

        if senha and confirma_senha:
            if senha != confirma_senha:
                raise forms.ValidationError('As senhas não conferem')
            else:
                return confirma_senha
