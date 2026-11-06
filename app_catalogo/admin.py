from django.contrib import admin
from .models import Autor, Libro, Editorial, Tema, Publicacion, Prestamo, Estudiante

admin.site.register(Autor)
admin.site.register(Libro)
admin.site.register(Editorial)
admin.site.register(Tema)
admin.site.register(Publicacion)
admin.site.register(Prestamo)
admin.site.register(Estudiante)