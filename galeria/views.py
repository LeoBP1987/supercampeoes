from django.shortcuts import render, redirect
from galeria.models import Times
from galeria.forms import TimeForms
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

    