from django.shortcuts import render, redirect
from campeonatos.models import Campeonato
from campeonatos.forms import CampeonatoForms
from django.contrib import messages

def campeonatos(request):

    campeonatos = Campeonato.objects.all()

    return render(request, 'campeonatos/campeonatos.html', {'campeonatos':campeonatos})

def novo_campeonato(request):

    forms = CampeonatoForms()

    if request.method == 'POST':

        forms = CampeonatoForms(request.POST)

        if forms.is_valid():
            novo_campeonato = forms.save(commit=False)
            
            novo_campeonato.usuario = request.user
            
            categoria = novo_campeonato.categoria

            if novo_campeonato.principal == 'SIM':
                novo_campeonato.pontuacao = categoria.pontuacao
            else:
                novo_campeonato.pontuacao = categoria.pontuacao/2

            novo_campeonato.save()

            messages.success(request, 'Campeonato cadastrado com sucesso!')
            return redirect('index')
        else:
            messages.error(request, 'Cadastro não realizado. Tente novamente.')
            return redirect('novo_campeonato')
            

    return render(request, 'campeonatos/novo_campeonato.html', {'forms':forms})

def editar_campeonato(request, campeonato_id):

    campeonato = Campeonato.objects.get(id=campeonato_id)

    forms = CampeonatoForms(instance=campeonato)

    if request.method == 'POST':

        forms = CampeonatoForms(request.POST, instance=campeonato)

        if forms.is_valid():
            campeonato_editado = forms.save(commit=False)
            
            categoria = campeonato_editado.categoria

            if campeonato_editado.principal == 'SIM':
                campeonato_editado.pontuacao = categoria.pontuacao
            else:
                campeonato_editado.pontuacao = categoria.pontuacao/2

            campeonato_editado.save()

            messages.success(request, 'Alteração realizada com sucesso!')
            return redirect('index')

    return render(request, 'campeonatos/editar_campeonato.html', {'forms':forms, 'campeonato_id':campeonato_id})

def deletar_campeonato(request, campeonato_id):
    
    campeonato = Campeonato.objects.get(id=campeonato_id)

    campeonato.delete()

    messages.success(request, 'Deleção realizada com sucesso.')

    return redirect('index')