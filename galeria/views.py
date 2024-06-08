from django.shortcuts import render, redirect
from galeria.models import Times
from galeria.forms import TimeForms
from django.contrib import messages

def index(request):

    times = Times.objects.all()

    return render(request, 'galeria/index.html', {'times':times})

def times(request, time_id):

    time = Times.objects.get(id=time_id)

    return render(request, 'galeria/times.html', {'time':time})

def ranking(request):
    return render(request, 'galeria/ranking.html')

def meus_times(request):
    return render(request, 'galeria/meus_times.html')

def novo_time(request):

    forms = TimeForms()

    if request.method == 'POST':
        forms = TimeForms(request.POST, request.FILES)

        if forms.is_valid():
            novo_time = forms.save(commit=False)
            novo_time.usuario = request.user
            novo_time.save()
            messages.success(request, 'Time Salvo com Sucesso!')
            return redirect('index')
        else:
            messages.error(request, 'Erro no cadastro. Tente novamente')
            return redirect('novo_time')

    return render(request, 'galeria/novo_time.html', {'forms':forms})