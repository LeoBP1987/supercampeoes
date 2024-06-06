from django.shortcuts import render

def index(request):
    return render(request, 'galeria/index.html')

def times(request):
    return render(request, 'galeria/times.html')

def ranking(request):
    return render(request, 'galeria/ranking.html')