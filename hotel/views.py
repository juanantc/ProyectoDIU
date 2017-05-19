from django.shortcuts import render

def index(request):
    return render(request, 'hotel/index.html')

def servicios(request):
    return render(request, 'hotel/servicios.html')

def galeria(request):
    return render(request, 'hotel/galeria.html')

def informacion(request):
    return render(request, 'hotel/informacion.html')

def foro(request):
    return render(request, 'hotel/foro.html')
