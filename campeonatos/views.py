from django.shortcuts import render, redirect
from campeonatos.models import Campeonato
from galeria.models import DeclararCampeao
from campeonatos.forms import CampeonatoForms, RkCampeonatosForms
from django.contrib import messages
from django.db.models import When, Case, IntegerField

def ordenar_campeonatos(tabela, time):

    if time == 0:
        campeonatos = tabela.objects.all().annotate(
            custom_order=Case(
                When(categoria__categoria='Nacional', then=1),
                When(categoria__categoria='Continental', then=2),
                When(categoria__categoria='Mundial', then=3),
                output_field=IntegerField()
            )
        ).order_by('custom_order')
    else:
        campeonatos = tabela.objects.filter(time=time).annotate(
            custom_order=Case(
                When(campeonato__categoria__categoria='Nacional', then=1),
                When(campeonato__categoria__categoria='Continental', then=2),
                When(campeonato__categoria__categoria='Mundial', then=3),
                output_field=IntegerField()
            )
        ).order_by('custom_order')

    return campeonatos

def campeonatos(request):

    campeonatos = ordenar_campeonatos(Campeonato, 0)

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

def ranking_campeonato(request):

    forms = RkCampeonatosForms()

    if request.method == 'POST':

        forms = RkCampeonatosForms(request.POST)

        if forms.is_valid():

            campeonato_escolhido = forms.cleaned_data['campeonato']

            titulos = DeclararCampeao.objects.filter(campeonato__nome_campeonato=campeonato_escolhido)

            dict_times = {}

            for titulo in titulos:
                if titulo.time.nome_curto not in dict_times:
                    titulos_time = DeclararCampeao.objects.filter(time=titulo.time, campeonato__nome_campeonato=campeonato_escolhido)
                    
                    soma_pontos = 0
                    for ttitulo in titulos_time:
                        soma_pontos += ttitulo.pontuacao

                    quantidade = 0
                    for ttitulo in titulos_time:
                        quantidade += ttitulo.quantidade    

                    dict_times[titulo.time.nome_curto]={
                        'time':titulo.time.nome_curto,
                        'simbolo': titulo.time.simbolo,
                        'quantidade': quantidade,
                        'pontuacao': soma_pontos    
                    }
            lista_time = list(dict_times.values())

            lista_time.sort(key=lambda x: x['pontuacao'], reverse=True)

            for idx, time in enumerate(lista_time, start=1):
                time['posicao']=idx

            return render(request, 'galeria/ranking_campeonato.html', {'lista':lista_time})
        
    return render(request, 'galeria/rk_escolha_campeonato.html', {'forms':forms})