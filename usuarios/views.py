from django.shortcuts import render, redirect
from django.contrib import auth, messages
from usuarios.forms import LoginForms, CadastroForms
from usuarios.models import UsuariosCustomizados

def login(request):

    forms = LoginForms()

    if request.method == 'POST':
        forms = LoginForms(request.POST)

        if forms.is_valid():
            login = forms['login'].value()
            senha = forms['senha'].value()
            
            usuario = auth.authenticate(
                request,
                username=login,
                password=senha
            )

            if usuario is not None:
                auth.login(request, usuario)
                return redirect('index')
            else:
                messages.error(request, 'Erro ao efetuar login. Tente novamente ou entre em contato com o adm da página!')
                return redirect('login')



    return render(request, 'usuarios/login.html', {'forms':forms})

def cadastro(request):

    forms = CadastroForms()

    if request.method == 'POST':
        forms = CadastroForms(request.POST)

        if forms.is_valid():
            
            if forms['senha'].value() != forms['confirma_senha'].value():
                messages.error(request, 'As senhas informadas não conferem!')
                return redirect('cadastro')
            
            login = forms['login'].value()
            
            if UsuariosCustomizados.objects.filter(username=login).exists():
                messages.error(request, 'Login de usuário já existe!')
                return redirect('cadastro')
            
            nome_completo = forms['nome_completo'].value()
            email = forms['email'].value()
            time = forms['time'].value()
            senha = forms['senha'].value()   

            usuario = UsuariosCustomizados.objects.create(
                nome_completo = nome_completo,
                email = email,
                time = time,
                username = login,
            )

            usuario.set_password(senha)

            usuario.save()

            messages.success(request, 'Cadastro realizado com sucesso!')

            return redirect('login')
    
    return render(request, 'usuarios/cadastro.html', {'forms':forms})

def logout(request):

    auth.logout(request)
    messages.success(request, 'Logout Efetuado com Sucesso!')

    return redirect('index')