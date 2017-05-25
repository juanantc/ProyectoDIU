from django.shortcuts import render

def index(request):
    return render(request, 'hotel/index.html')

def servicios(request):
    return render(request, 'hotel/servicios.html')

def galeria(request):
    return render(request, 'hotel/galeria.html')

def ubicacion(request):
    return render(request, 'hotel/ubicacion.html')

def instalaciones(request):
    return render(request, 'hotel/instalaciones.html')

def parking(request):
    return render(request, 'hotel/parking.html')

def info(request):
    return render(request, 'hotel/info.html')

def contacto(request):
    return render(request, 'hotel/contacto.html')

def foro(request):
    return render(request, 'hotel/foro.html')
