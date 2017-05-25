from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^servicios$', views.servicios, name='servicios'),
    url(r'^galeria$', views.galeria, name='galeria'),
    url(r'^foro$', views.foro, name='foro'),
    url(r'^ubicacion$', views.ubicacion, name='ubicacion'),
    url(r'^instalaciones$', views.instalaciones, name='instalaciones'),
    url(r'^parking$', views.parking, name='parking'),
    url(r'^info$', views.info, name='info'),
    url(r'^contacto$', views.contacto, name='contacto'),
]
