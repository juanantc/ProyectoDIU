from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from .forms import login_form
from django.contrib.auth.models import User
from hotel.models import Comentarios, Reservas
import random

def index(request):
    form = login_form()
    context = {'form': form}

    if request.method == 'POST':
        usuario = request.POST.get('username')
        passw = request.POST.get('password')

        user = authenticate(username=usuario, password=passw)

        if user is not None and user.is_active:
            login(request, user)

    if request.user.is_authenticated():
        context['mensaje'] =  u'Bienvenido %s' % (request.user)
    else:
        context['form'] = form

    return render(request, 'hotel/index.html', context)

def salir(request):
    logout(request)
    form = login_form()
    context = {'form': form}
    return render (request,'hotel/index.html',context)

def reservas(request):
    form = login_form()
    context = {'form': form}

    context['Reservas'] = Reservas.objects.all()[:1]

    if request.user.is_authenticated():
        context['mensaje'] =  u'Bienvenido %s' % (request.user)
        return render(request,'hotel/reservas.html',context)

    return render(request,'hotel/index.html')

def reservar3(request):
    paso4 = 1
    context = {'paso4': paso4}

    if request.method == 'POST':
        context['dni'] = request.POST.get('dni')

    return render(request,'hotel/reserva.html',context)

def reservar2(request):
    paso3 = 1
    context = {'paso3': paso3}

    if request.method == 'POST':
        context['fecha_e'] = request.POST.get('fecha_e')
        context['fecha_s'] = request.POST.get('fecha_s')
        context['adultos'] = request.POST.get('adultos')
        context['ninos'] = request.POST.get('ninos')
        context['habitacion'] = request.POST.get('habitacion')
        context['dni'] = request.POST.get('dni')
        r = Reservas(fecha_e = context['fecha_e'], fecha_s = context['fecha_s'], habitacion = context['habitacion'], usuario = context['dni'], adultos = context['adultos'],ninos = context['ninos'])
        r.save()

        usuario = context['dni']
        passwd = context['dni']
        user = User.objects.create_user(usuario, 'example@example.com', passwd)
        user.save()

    return render(request,'hotel/reserva.html',context)


def reservar1(request):
    paso2 = 1
    context = {'paso2': paso2}
    if request.method == 'POST':
        context['fecha_e'] = request.POST.get('datepicker1')
        context['fecha_s'] = request.POST.get('datepicker2')
        context['adultos'] = request.POST.get('adultos')
        context['ninos'] = request.POST.get('ninos')
        return render(request,'hotel/reserva.html',context)
    else:
        return render(request,'hotel/reserva.html')



def reserva(request):
    paso1 = 1
    context = {'paso1': paso1}

    if request.user.is_authenticated():
        context['mensaje'] =  u'Bienvenido %s' % (request.user)

    return render(request, 'hotel/reserva.html',context)

def servicios(request):
    form = login_form()
    context = {'form': form}

    if request.user.is_authenticated():
        context['mensaje'] =  u'Bienvenido %s' % (request.user)

    return render(request, 'hotel/servicios.html',context)

def galeria(request):
    form = login_form()
    context = {'form': form}

    if request.user.is_authenticated():
        context['mensaje'] =  u'Bienvenido %s' % (request.user)

    return render(request, 'hotel/galeria.html',context)

def ubicacion(request):
    form = login_form()
    context = {'form': form}

    if request.user.is_authenticated():
        context['mensaje'] =  u'Bienvenido %s' % (request.user)

    return render(request, 'hotel/ubicacion.html',context)

def instalaciones(request):
    form = login_form()
    context = {'form': form}

    if request.user.is_authenticated():
        context['mensaje'] =  u'Bienvenido %s' % (request.user)

    return render(request, 'hotel/instalaciones.html',context)

def parking(request):
    form = login_form()
    context = {'form': form}

    if request.user.is_authenticated():
        context['mensaje'] =  u'Bienvenido %s' % (request.user)

    return render(request, 'hotel/parking.html',context)

def info(request):
    form = login_form()
    context = {'form': form}

    if request.user.is_authenticated():
        context['mensaje'] =  u'Bienvenido %s' % (request.user)

    return render(request, 'hotel/info.html',context)

def contacto(request):
    form = login_form()
    context = {'form': form}

    if request.user.is_authenticated():
        context['mensaje'] =  u'Bienvenido %s' % (request.user)

    return render(request, 'hotel/contacto.html',context)

def foro(request):
    form = login_form()
    context = {'form': form}

    if request.user.is_authenticated():
        context['mensaje'] =  u'Bienvenido %s' % (request.user)

    if request.method == 'POST':
        usuario = request.user
        texto = request.POST.get('texto')
        c = Comentarios(usuario = usuario, texto = texto)
        c.save()

    context['Comentarios'] = Comentarios.objects.all()[:10]

    return render(request, 'hotel/foro.html',context)
