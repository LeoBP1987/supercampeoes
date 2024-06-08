from django.shortcuts import render

def Campeonatos(request):
    return render(request, 'campeonatos/campeonatos.html')