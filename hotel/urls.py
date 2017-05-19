from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^servicios$', views.servicios, name='servicios'),
    url(r'^galeria$', views.galeria, name='galeria'),
    url(r'^informacion$', views.informacion, name='informacion'),
    url(r'^foro$', views.foro, name='foro'),


]
