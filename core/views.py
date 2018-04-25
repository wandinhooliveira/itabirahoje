from django.shortcuts import render
import html

from .models import noticia
# Create your views here.
url_img = 'http://www.liderancacomvoce.com.br/statics/images/'
def index(request):
    ultimas_noticias = noticia.objects.order_by('-data')[:10]
    noticia_capa = noticia.objects.filter(capa=1).order_by('-data')[:1]
    noticia_capa2 = noticia.objects.filter(capa=2).order_by('-data')[:1]
    noticia_capa3 = noticia.objects.filter(capa=3).order_by('-data')[:1]
    context = {'ultimas_noticias': ultimas_noticias,
               'noticia_capa': noticia_capa,
               'noticia_capa2': noticia_capa2,
               'noticia_capa3': noticia_capa3,
               'url_img': url_img}
    return render(request, 'index.html' , context)

def noticia_show(request, slug):
    noticia_mostrar = noticia.objects.filter(slug=slug)[:1]
    categoria = ''
    for noti in noticia_mostrar:
        categoria = noti.categoria

    ultimas_noticias = noticia.objects.filter(categoria=categoria).order_by('-data')[:8]


    context = {'noticia_mostrar': noticia_mostrar,
               'url_img': url_img,
               'ultimas_noticias': ultimas_noticias}

    return render(request, 'noticia.html', context)

def categoria_show(request, categoria):
    lista_noticias = noticia.objects.filter(categoria=categoria.capitalize()).order_by('-data')
    context = {'lista_noticias': lista_noticias,
               'url_img': url_img,}

    return render(request, 'categoria.html', context)

def ultimas_noticias(request):
    ultimas_noticias = noticia.objects.order_by('-data')[:20]
    context = {'lista_noticias': ultimas_noticias,
               'url_img': url_img}
    return render(request, 'categoria.html', context)

def busca_noticias(request):
    busca = request.GET.get('busca')
    lista_noticias = noticia.objects.filter(titulo__contains=busca).order_by('-data')

    context = {'lista_noticias': lista_noticias,
               'url_img': url_img, }
    return render(request, 'categoria.html', context)