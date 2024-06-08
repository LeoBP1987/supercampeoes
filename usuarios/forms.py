from django import forms

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