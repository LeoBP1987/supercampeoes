from django.shortcuts import render, redirect
from galeria.models import Times, DeclararCampeao
from galeria.forms import TimeForms, CampeoesForms
from django.contrib import messages
import logging

def index(request):

    times = Times.objects.all()

    return render(request, 'galeria/index.html', {'times':times})

def times(request, time_id):

    time = Times.objects.get(id=time_id)

    return render(request, 'galeria/times.html', {'time':time})

def ranking(request):
    return render(request, 'galeria/ranking.html')

def meus_times(request):

    logado = request.user
    times = Times.objects.filter(usuario=logado)

    return render(request, 'galeria/meus_times.html', {'times':times})

def novo_time(request):

    forms = TimeForms()

    if request.method == 'POST':

        forms = TimeForms(request.POST, request.FILES)

        if forms.is_valid(): 
            novo_time = forms.save(commit=False)
            novo_time.usuario = request.user
            novo_time.save()
            messages.success(request, 'Cadastro efetuado com Sucesso')
            return redirect('index')
        else:
            messages.error(request, 'Erro ao cadastrar novo time. Tente novamente.')
            return redirect('index')

    return render(request, 'galeria/novo_time.html', {'forms':forms})

def editar_time(request, time_id):

    time = Times.objects.get(id=time_id)

    forms = TimeForms(instance=time)

    if request.method == 'POST':

        forms = TimeForms(request.POST, request.FILES, instance=time)

        if forms.is_valid():
            forms.save()
            messages.success(request, 'Alterações Salvas com sucesso')
            return redirect('index')

    return render(request, 'galeria/editar_time.html', {'forms':forms,'time_id':time_id})

def deletar_time(request, time_id):

    time = Times.objects.get(id=time_id)

    time.delete()

    messages.success(request, 'Deleção realizada com sucesso!')

    return redirect('index')

def titulos(request, time_id):

    time = Times.objects.get(id=time_id)
    
    titulos = DeclararCampeao.objects.filter(time=time)

    return render(request, 'galeria/titulos.html', {'time':time, 'titulos':titulos})

def novo_titulo(request, time_id):

    time = Times.objects.get(id=time_id)

    forms = CampeoesForms()

    if request.method == 'POST':

        forms = CampeoesForms(request.POST)

        if forms.is_valid():
            novo_titulo = forms.save(commit=False)
            novo_titulo.time = time
            novo_titulo.pontuacao = novo_titulo.quantidade * novo_titulo.campeonato.pontuacao
            novo_titulo.save()
            messages.success(request, 'Cadastro realizado com Sucesso!')
            return redirect('index')
        else:
            messages.error(request, 'Erro ao cadastro. Tente novamente.')

    return render(request, 'galeria/novo_titulo.html', {'forms':forms, 'time':time})

def editar_titulo(request, titulo_id):

    titulo = DeclararCampeao.objects.get(id=titulo_id)

    forms = CampeoesForms(instance=titulo)

    if request.method == 'POST':

        forms = CampeoesForms(request.POST, instance=titulo)

        if forms.is_valid():
            titulo_editado = forms.save(commit=False)
            titulo_editado.pontuacao = titulo_editado.quantidade * titulo_editado.campeonato.pontuacao
            titulo_editado.save()
            messages.success(request, 'Alteração realizada com Sucesso!')
            return redirect('index')

    return render(request, 'galeria/editar_titulo.html', {'forms':forms, 'titulo':titulo})

def deletar_titulo(request, titulo_id):
    
    titulo = DeclararCampeao.objects.get(id=titulo_id)

    titulo.delete()

    messages.success(request, 'Deleção realizada com sucesso!')

    return redirect('index')

def ranking_geral(request):
    return render(request, 'galeria/ranking_geral.html')

    