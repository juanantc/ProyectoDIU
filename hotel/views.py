from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from .forms import login_form
from django.contrib.auth.models import User
from hotel.models import Comentarios

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
    return render (request, 'hotel/index.html',context)

def reserva(request):
    return render (request, 'hotel/reserva.html')

def registro(request):
	form = register_form()
	context = {'form': form}
	if request.method == 'POST':
		form = register_form(request.POST)
		if form.is_valid():
			usuario = request.POST.get('username')
			passw = request.POST.get('password')

			user = User.objects.create_user(usuario,passw)
			user.save()

			return render (request, 'hotel/index.html')

	return render (request, 'bares/registro.html', context)

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
