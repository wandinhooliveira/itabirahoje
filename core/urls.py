from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('noticias/<slug>', views.noticia_show, name='noticia_show'),
    path('ultimas', views.ultimas_noticias, name='ultimas_noticias'),
    path('noticias', views.ultimas_noticias, name='ultimas_noticias'),
    path('busca', views.busca_noticias, name='buscar_noticias'),
    path('<categoria>', views.categoria_show, name='categoria_show'),
]