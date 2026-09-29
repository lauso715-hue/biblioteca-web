from django.shortcuts import render
from .models import Categoria, Libro   


def bienvenida(request):
    return render(request, 'bienvenida.html')


def inicio(request):
    categorias = Categoria.objects.all()
    libros = Libro.objects.all()       
    return render(request, 'inicio.html', {
        'categorias': categorias,
        'libros': libros,
    })


def despedida(request):
    return render(request, 'despedida.html')