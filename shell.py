from datetime import date
from decimal import Decimal
from app_catalogo.models import Tema, Editorial, Autor, Libro, Publicacion

# =========================
# 1. TEMAS
# =========================
tema_ficcion = Tema.objects.create(Nombre_Tema="Ficción")
tema_misterio = Tema.objects.create(Nombre_Tema="Misterio")
tema_biografia = Tema.objects.create(Nombre_Tema="Biografía")

# =========================
# 2. EDITORIALES
# =========================
editorial_anagrama = Editorial.objects.create(
    Nombre_Editorial="Anagrama",
    Direccion="Calle de la Cruz #12, Barcelona"
)

editorial_penguin = Editorial.objects.create(
    Nombre_Editorial="Penguin Random House",
    Direccion="Av. 5 #45-89, Madrid"
)

editorial_fce = Editorial.objects.create(
    Nombre_Editorial="Fondo de Cultura Económica",
    Direccion="Carrera 15 #22-10, Bogotá"
)

# =========================
# 3. AUTORES
# =========================
autor6 = Autor.objects.create(
    Num_Documento="2000000001",
    Tipo_Documento="Cédula de Ciudadania",
    Nombre="Jorge Luis",
    Apellido="Borges",
    Correo="jorge.borges@example.com",
    Telefono="3006666666",
    Fecha_Nacimiento=date(1899, 8, 24),
    Genero="Masculino",
    Rol="Autor",
    Nacionalidad="Argentina",
    Biografia="Escritor argentino, maestro del cuento corto y la ficción.",
    Estado="Activo"
)

autor7 = Autor.objects.create(
    Num_Documento="2000000002",
    Tipo_Documento="Pasaporte",
    Nombre="Agatha",
    Apellido="Christie",
    Correo="agatha.christie@example.com",
    Telefono="3007777777",
    Fecha_Nacimiento=date(1890, 9, 15),
    Genero="Femenino",
    Rol="Autor",
    Nacionalidad="Británica",
    Biografia="Escritora británica, la novelista de misterio más famosa.",
    Estado="Activo"
)

autor8 = Autor.objects.create(
    Num_Documento="2000000003",
    Tipo_Documento="Cédula Extranjer",
    Nombre="Stephen",
    Apellido="King",
    Correo="stephen.king@example.com",
    Telefono="3008888888",
    Fecha_Nacimiento=date(1947, 9, 21),
    Genero="Masculino",
    Rol="Autor",
    Nacionalidad="Estadounidense",
    Biografia="Autor de novelas de terror y suspenso.",
    Estado="Activo"
)

autor9 = Autor.objects.create(
    Num_Documento="2000000004",
    Tipo_Documento="Pasaporte",
    Nombre="Haruki",
    Apellido="Murakami",
    Correo="haruki.murakami@example.com",
    Telefono="3009999999",
    Fecha_Nacimiento=date(1949, 1, 12),
    Genero="Masculino",
    Rol="Autor",
    Nacionalidad="Japonesa",
    Biografia="Escritor japonés contemporáneo de gran popularidad.",
    Estado="Activo"
)

autor10 = Autor.objects.create(
    Num_Documento="2000000005",
    Tipo_Documento="Cédula de Ciudadania",
    Nombre="Jane",
    Apellido="Austen",
    Correo="jane.austen@example.com",
    Telefono="3010000000",
    Fecha_Nacimiento=date(1775, 12, 16),
    Genero="Femenino",
    Rol="Autor",
    Nacionalidad="Británica",
    Biografia="Novelista británica conocida por sus críticas sociales y romances.",
    Estado="Activo"
)

# =========================
# 4. LIBROS
# =========================
libro11 = Libro.objects.create(
    Titulo="Ficciones",
    Codigo_Barras="LIB-0011",
    Estado="Activo",
    Ubicacion="Estante F-1",
    Precio=Decimal("60000.00")
)

libro12 = Libro.objects.create(
    Titulo="Asesinato en el Orient Express",
    Codigo_Barras="LIB-0012",
    Estado="Activo",
    Ubicacion="Estante F-2",
    Precio=Decimal("38000.00")
)

libro13 = Libro.objects.create(
    Titulo="El resplandor",
    Codigo_Barras="LIB-0013",
    Estado="Activo",
    Ubicacion="Estante G-1",
    Precio=Decimal("55000.00")
)

libro14 = Libro.objects.create(
    Titulo="Tokio Blues",
    Codigo_Barras="LIB-0014",
    Estado="Activo",
    Ubicacion="Estante G-2",
    Precio=Decimal("49000.00")
)

libro15 = Libro.objects.create(
    Titulo="Orgullo y prejuicio",
    Codigo_Barras="LIB-0015",
    Estado="Activo",
    Ubicacion="Estante H-1",
    Precio=Decimal("36000.00")
)

libro16 = Libro.objects.create(
    Titulo="El Aleph",
    Codigo_Barras="LIB-0016",
    Estado="Activo",
    Ubicacion="Estante H-2",
    Precio=Decimal("58000.00")
)

libro17 = Libro.objects.create(
    Titulo="Diez negritos",
    Codigo_Barras="LIB-0017",
    Estado="Activo",
    Ubicacion="Estante I-1",
    Precio=Decimal("40000.00")
)

libro18 = Libro.objects.create(
    Titulo="It",
    Codigo_Barras="LIB-0018",
    Estado="Activo",
    Ubicacion="Estante I-2",
    Precio=Decimal("65000.00")
)

libro19 = Libro.objects.create(
    Titulo="Kafka en la orilla",
    Codigo_Barras="LIB-0019",
    Estado="Activo",
    Ubicacion="Estante J-1",
    Precio=Decimal("53000.00")
)

libro20 = Libro.objects.create(
    Titulo="Sentido y sensibilidad",
    Codigo_Barras="LIB-0020",
    Estado="Activo",
    Ubicacion="Estante J-2",
    Precio=Decimal("37000.00")
)

# =========================
# 5. PUBLICACIONES
# =========================
Publicacion.objects.create(
    Descripcion="Colección de cuentos fantásticos y filosóficos.",
    Edicion="2da",
    Fecha_Publicacion=date(1944, 1, 1),
    ISBN="9788420633134",
    Id_Libro=libro11,
    Id_Editorial=editorial_anagrama,
    Id_Tema=tema_ficcion,
    Num_Documento=autor6
)

Publicacion.objects.create(
    Descripcion="Misterio clásico de Hércules Poirot.",
    Edicion="1ra",
    Fecha_Publicacion=date(1934, 1, 1),
    ISBN="9788498385356",
    Id_Libro=libro12,
    Id_Editorial=editorial_penguin,
    Id_Tema=tema_misterio,
    Num_Documento=autor7
)

Publicacion.objects.create(
    Descripcion="Novela de terror psicológico en un hotel aislado.",
    Edicion="1ra",
    Fecha_Publicacion=date(1977, 1, 28),
    ISBN="9788497593882",
    Id_Libro=libro13,
    Id_Editorial=editorial_penguin,
    Id_Tema=tema_ficcion,
    Num_Documento=autor8
)

Publicacion.objects.create(
    Descripcion="Novela coming-of-age ambientada en Japón.",
    Edicion="1ra",
    Fecha_Publicacion=date(1987, 9, 4),
    ISBN="9788483835043",
    Id_Libro=libro14,
    Id_Editorial=editorial_fce,
    Id_Tema=tema_ficcion,
    Num_Documento=autor9
)

Publicacion.objects.create(
    Descripcion="Novela romántica y crítica social victoriana.",
    Edicion="1ra",
    Fecha_Publicacion=date(1813, 1, 28),
    ISBN="9788491050296",
    Id_Libro=libro15,
    Id_Editorial=editorial_anagrama,
    Id_Tema=tema_ficcion,
    Num_Documento=autor10
)

Publicacion.objects.create(
    Descripcion="Libro de cuentos que incluye el famoso relato homónimo.",
    Edicion="3ra",
    Fecha_Publicacion=date(1949, 1, 1),
    ISBN="9788420633141",
    Id_Libro=libro16,
    Id_Editorial=editorial_anagrama,
    Id_Tema=tema_ficcion,
    Num_Documento=autor6
)

Publicacion.objects.create(
    Descripcion="Novela de misterio con diez sospechosos en una isla.",
    Edicion="1ra",
    Fecha_Publicacion=date(1939, 11, 6),
    ISBN="9788498385363",
    Id_Libro=libro17,
    Id_Editorial=editorial_penguin,
    Id_Tema=tema_misterio,
    Num_Documento=autor7
)

Publicacion.objects.create(
    Descripcion="Épica novela de terror sobre un payaso maligno.",
    Edicion="1ra",
    Fecha_Publicacion=date(1986, 9, 15),
    ISBN="9788497593899",
    Id_Libro=libro18,
    Id_Editorial=editorial_penguin,
    Id_Tema=tema_ficcion,
    Num_Documento=autor8
)

Publicacion.objects.create(
    Descripcion="Novela surrealista con dos tramas paralelas.",
    Edicion="1ra",
    Fecha_Publicacion=date(2002, 9, 12),
    ISBN="9788483835050",
    Id_Libro=libro19,
    Id_Editorial=editorial_fce,
    Id_Tema=tema_ficcion,
    Num_Documento=autor9
)

Publicacion.objects.create(
    Descripcion="Historia de las hermanas Dashwood y sus romances.",
    Edicion="1ra",
    Fecha_Publicacion=date(1811, 10, 30),
    ISBN="9788491050302",
    Id_Libro=libro20,
    Id_Editorial=editorial_anagrama,
    Id_Tema=tema_ficcion,
    Num_Documento=autor10
)

# =========================
# VERIFICACIÓN
# =========================
print("Temas:", Tema.objects.count())
print("Editoriales:", Editorial.objects.count())
print("Autores:", Autor.objects.count())
print("Libros:", Libro.objects.count())
print("Publicaciones:", Publicacion.objects.count())