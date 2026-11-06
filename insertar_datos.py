import os
import django
import datetime

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pr_biblioteca_web.settings')
django.setup()

from app_catalogo.models import Autor, Editorial, Tema, Libro, Publicacion

LIBROS = [ 
    {"id": 1, "titulo": "El río de las palabras", "autor": "Marta Ríos", "anio": 1998, "genero": "novela", "disponible": True}, 
    {"id": 2, "titulo": "Noches de lluvia", "autor": "Julián Ortega", "anio": 2005, "genero": "novela", "disponible": False}, 
    {"id": 3, "titulo": "Python desde cero", "autor": "Ana Ruiz", "anio": 2021, "genero": "tecnologia", "disponible": True}, 
    {"id": 4, "titulo": "El universo en tu bolsillo", "autor": "Carlos Vega", "anio": 2012, "genero": "ciencia", "disponible": True}, 
    {"id": 5, "titulo": "Cuentos del Magdalena", "autor": "Marta Ríos", "anio": 1987, "genero": "novela", "disponible": True}, 
    {"id": 6, "titulo": "Django paso a paso", "autor": "Laura Méndez", "anio": 2024, "genero": "tecnologia", "disponible": False},
    # Los 4 nuevos libros:
    {"id": 7, "titulo": "Código limpio", "autor": "Robert Martin", "anio": 2008, "genero": "tecnologia", "disponible": True},
    {"id": 8, "titulo": "Historia del tiempo", "autor": "Stephen Hawking", "anio": 1988, "genero": "ciencia", "disponible": True},
    {"id": 9, "titulo": "Crónica de una muerte anunciada", "autor": "Gabriel García", "anio": 1981, "genero": "novela", "disponible": True},
    {"id": 10, "titulo": "El arte de programar", "autor": "Donald Knuth", "anio": 1968, "genero": "tecnologia", "disponible": False},
]

print("⏳ Insertando los 10 libros...")

# Crear una Editorial por defecto para todos
editorial, _ = Editorial.objects.get_or_create(Nombre_Editorial="Editorial General", defaults={'Direccion': "Bogotá"})

for lib in LIBROS:
    # 1. Tema
    tema, _ = Tema.objects.get_or_create(Nombre_Tema=lib['genero'].capitalize())

    # 2. Autor (Separamos el nombre y apellido)
    partes_nombre = lib['autor'].split(' ', 1)
    nombre = partes_nombre[0]
    apellido = partes_nombre[1] if len(partes_nombre) > 1 else "Apellido"

    autor, _ = Autor.objects.get_or_create(
        Nombre=nombre, Apellido=apellido,
        defaults={
            'Num_Documento': f"DOC-{lib['id']}", 
            'Tipo_Documento': "Cédula de Ciudadania",
            'Correo': f"autor{lib['id']}@test.com", 
            'Telefono': "123",
            'Fecha_Nacimiento': datetime.date(1970, 1, 1), 
            'Genero': "Masculino",
            'Rol': "Autor", 
            'usuario': f"user{lib['id']}", 
            'contrasena': "123",
            'estado': "Aprobado", 
            'Nacionalidad': "Colombiana", 
            'Biografia': "Biografía del autor", 
            'Estado': "Activo"
        }
    )

    # 3. Libro
    estado_libro = "Activo" if lib['disponible'] else "Inactivo"
    
    libro, _ = Libro.objects.get_or_create(
        Titulo=lib['titulo'],
        defaults={
            'Codigo_Barras': f"CB-{lib['id']:03d}", 
            'Estado': estado_libro,
            'Ubicacion': f"Estante {chr(64+lib['id'])}", # Esto genera A, B, C...
            'Precio': 50000.00
        }
    )

    # 4. Publicacion
    Publicacion.objects.get_or_create(
        Id_Libro=libro,
        defaults={
            'Descripcion': f"Edición de {lib['titulo']}", 
            'Edicion': "1ra",
            'Fecha_Publicacion': datetime.date(lib['anio'], 1, 1), 
            'ISBN': f"ISBN-{lib['id']}", 
            'Id_Editorial': editorial, 
            'Id_Tema': tema, 
            'Num_Documento': autor
        }
    )

print("✅ ¡Los 10 libros fueron insertados correctamente!")