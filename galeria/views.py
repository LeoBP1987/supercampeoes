from django.shortcuts import render, redirect
from galeria.models import Times, DeclararCampeao
from galeria.forms import TimeForms, CampeoesForms, EstadoForms
from campeonatos.models import Categoria
from django.contrib import messages
from campeonatos.views import ordenar_campeonatos
import logging

def index(request):

    times = Times.objects.all().order_by('?')

    return render(request, 'galeria/index.html', {'times':times})

def times(request, time_id):

    time = Times.objects.get(id=time_id)

    return render(request, 'galeria/times.html', {'time':time})

def ranking(request):
    return render(request, 'galeria/ranking.html')

def meus_times(request):

    logado = request.user
    times = Times.objects.filter(usuario=logado).order_by('data_registro')

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

    return render(request, 'galeria/editar_time.html', {'forms':forms,'time':time})

def deletar_time(request, time_id):

    time = Times.objects.get(id=time_id)

    time.delete()

    messages.success(request, 'Deleção realizada com sucesso!')

    return redirect('index')

def titulos(request, time_id):

    time = Times.objects.get(id=time_id)
    
    titulos = ordenar_campeonatos(DeclararCampeao, time)

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

    time = titulo.time

    forms = CampeoesForms(instance=titulo)    

    if request.method == 'POST':

        forms = CampeoesForms(request.POST, instance=titulo)

        if forms.is_valid():
            titulo_editado = forms.save(commit=False)
            titulo_editado.pontuacao = titulo_editado.quantidade * titulo_editado.campeonato.pontuacao
            titulo_editado.save()
            messages.success(request, 'Alteração realizada com Sucesso!')
            return redirect('index')

    return render(request, 'galeria/editar_titulo.html', {'forms':forms, 'titulo':titulo, 'time':time})

def deletar_titulo(request, titulo_id):
    
    titulo = DeclararCampeao.objects.get(id=titulo_id)

    titulo.delete()

    messages.success(request, 'Deleção realizada com sucesso!')

    return redirect('index')

def gerar_ranking(categoria_ranking):

    if categoria_ranking == 'Geral':
        titulos = DeclararCampeao.objects.all()
    else:
        categoria = Categoria.objects.get(categoria=categoria_ranking)
        titulos = DeclararCampeao.objects.filter(campeonato__categoria=categoria)

    dict_times = {}    

    for titulo in titulos:
        if titulo.time.nome_curto not in dict_times:
            if categoria_ranking == 'Geral':
                titulos_time = DeclararCampeao.objects.filter(time=titulo.time)
            else:
                titulos_time = DeclararCampeao.objects.filter(campeonato__categoria=categoria, time=titulo.time)

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

    return lista_time

def ranking_geral(request):

    lista_time = gerar_ranking('Geral')

    return render(request, 'galeria/ranking_geral.html', {'lista': lista_time})

def ranking_nacional(request):

    lista_time = gerar_ranking('Nacional')

    return render(request, 'galeria/ranking_nacional.html', {'lista':lista_time})

def ranking_continental(request):
    
    lista_time = gerar_ranking('Continental')

    return render(request, 'galeria/ranking_continental.html', {'lista':lista_time})

def ranking_mundial(request):
    
    lista_time = gerar_ranking('Mundial')

    return render(request, 'galeria/ranking_mundial.html', {'lista':lista_time})

def ranking_posicoes(request, time_id):
    
    geral = ''
    nacional = ''
    continental = ''
    mundial = ''

    time = Times.objects.get(id=time_id)

    lista_geral = gerar_ranking('Geral')
    lista_nacional = gerar_ranking('Nacional')
    lista_continental = gerar_ranking('Continental')
    lista_mundial = gerar_ranking('Mundial')

    dict_time = {}

    for ttime in lista_geral:
        if ttime['time'] == time.nome_curto:
            geral = ttime['posicao']
    
    for ttime in lista_nacional:
        if ttime['time'] == time.nome_curto:
            nacional = ttime['posicao']

    for ttime in lista_continental:
        if ttime['time'] == time.nome_curto:
            continental = ttime['posicao']

    for ttime in lista_mundial:
        if ttime['time'] == time.nome_curto:
            mundial = ttime['posicao']

    dict_time[time.nome_curto]={
        'geral': f'{geral}º' if geral else '#',
        'nacional': f'{nacional}º' if nacional else '#',
        'continental': f'{continental}º' if continental else '#',
        'mundial': f'{mundial}º' if mundial else '#'
    }

    lista_time = list(dict_time.values())

    return render(request, 'galeria/ranking_posicoes.html', {'time':time, 'lista':lista_time})

def mascote(request, time_id):

    time = Times.objects.get(id=time_id)

    return render(request, 'galeria/mascote.html', {'time':time})

def ranking_estado(request):
    
    forms = EstadoForms()

    if request.method == 'POST':

        forms = EstadoForms(request.POST)

        if forms.is_valid():

            estado_escolhido = forms.cleaned_data['estado']

            lista_times = []

            times = Times.objects.all()

            for time in times:
                if time.estado == estado_escolhido:
                    lista_times.append(time)

            titulos = DeclararCampeao.objects.none()

            for time in lista_times:
                titulos = titulos | DeclararCampeao.objects.filter(time=time)

            dict_times = {}

            for titulo in titulos:
                if titulo.time.nome_curto not in dict_times:
                    titulos_time = DeclararCampeao.objects.filter(time=titulo.time)
                    
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

            return render(request, 'galeria/ranking_estado.html', {'lista':lista_time})
        
    return render(request, 'galeria/rk_escolha_estado.html', {'forms':forms})

def buscar(request):
    times = Times.objects.all().order_by('?')

    if 'buscar' in request.GET:
        nome_a_buscar = request.GET['buscar']
        if nome_a_buscar:
            times = Times.objects.filter(nome_completo__icontains=nome_a_buscar)

    return render(request, 'galeria/buscar.html', {'times':times})