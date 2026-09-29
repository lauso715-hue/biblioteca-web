from django.db import models

class Categoria(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(blank=True, null=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Categoría"
        verbose_name_plural = "Categorías"
        ordering = ['nombre']

    def __str__(self):
        return self.nombre

class Persona(models.Model):
    GENERO_CHOICES = [
        ('FEMENINO', 'Femenino'),
        ('MASCULINO', 'Masculino'),
        ('OTRO', 'Otro'),
        ('PREFIERO_NO_DECIRLO', 'Prefiero no decirlo'),
    ]

    ROL_CHOICES = [
        ('ESTUDIANTE', 'Estudiante'),
        ('AUTOR', 'Autor'),
    ]

    TIPO_DOCUMENTO_CHOICES = [
        ('DNI', 'Documento de Identidad'),
        ('PASSPORT', 'Pasaporte'),
        ('CEDULA', 'Cedula de Ciudadanía'),
        ('OTRO', 'Otro'),
    ]

    numero_documento = models.CharField(primary_key=True, max_length=45)
    nombre = models.CharField(max_length=45)
    apellido = models.CharField(max_length=45)
    correo = models.EmailField(max_length=100, unique=True)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    genero = models.CharField(max_length=20, choices=GENERO_CHOICES, null=True, blank=True)
    rol = models.CharField(max_length=20, choices=ROL_CHOICES)
    tipo_documento = models.CharField(max_length=45, choices=TIPO_DOCUMENTO_CHOICES)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class Autor(models.Model):
    ESTADO_CHOICES = [
        ('ACTIVO', 'Activo'),
        ('INACTIVO', 'Inactivo'),
    ]

    numero_documento = models.OneToOneField(
        Persona, on_delete=models.CASCADE, primary_key=True, related_name='autor'
    )
    nacionalidad = models.CharField(max_length=45, null=True, blank=True)       
    biografia = models.CharField(max_length=500, null=True, blank=True)         
    estado = models.CharField(max_length=45, choices=ESTADO_CHOICES)            # antes: Estado

    def __str__(self):
        return f"{self.numero_documento.nombre} {self.numero_documento.apellido}"


class Estudiante(models.Model):
    numero_documento = models.OneToOneField(
        Persona, on_delete=models.CASCADE, primary_key=True, related_name='estudiante'
    )
    direccion = models.CharField(max_length=100)
    telefono = models.CharField(max_length=45, unique=True)
    grado_escolar = models.CharField(max_length=45, null=True, blank=True)

    def __str__(self):
        return f"{self.numero_documento.nombre} {self.numero_documento.apellido}"

class Editorial(models.Model):
    id_Editorial = models.AutoField(primary_key=True)
    direccion = models.CharField(max_length=100) 
    nombre_editorial = models.CharField(max_length=100) 

    def __str__(self):
        return self.nombre_editorial

class Tema(models.Model):
    id_tema = models.AutoField(primary_key=True)
    nombre_tema = models.CharField(max_length=100) 

    def __str__(self):
        return self.nombre_tema

class Libro(models.Model):
    ESTADO_CHOICES = [
        ('DISPONIBLE', 'Disponible'),
        ('PRESTADO', 'Prestado'),
        ('MANTENIMIENTO', 'En mantenimiento'),
    ]

    codigo_barras = models.AutoField(primary_key=True, unique=True)
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES)
    ubicacion = models.CharField(max_length=45)
    precio = models.DecimalField(max_digits=8, decimal_places=2) 
    titulo = models.CharField(max_length=200) 

    autor = models.ForeignKey(
        Autor,
        on_delete=models.CASCADE,
        related_name='libros'
    )

    def __str__(self):
        return self.titulo

class Publicacion(models.Model):
    id_publicacion = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=200) 
    edicion = models.CharField(max_length=45)
    ISBN = models.CharField(max_length=45, unique=True) 
    fecha_publicacion = models.DateField(auto_now_add=True)

    autor = models.ForeignKey(
        Autor,
        on_delete=models.CASCADE,
        related_name='publicaciones'
    )

    editorial = models.ForeignKey(
        Editorial,
        on_delete=models.CASCADE,
        related_name='publicaciones'
    )

    tema = models.ForeignKey(
        Tema,
        on_delete=models.CASCADE,
        related_name='publicaciones'
    )

    libro = models.ForeignKey(
        Libro,
        on_delete=models.CASCADE,
        related_name='publicaciones'
    )

    def __str__(self):
        return self.titulo

class Prestamo(models.Model):
    id_prestamo = models.AutoField(primary_key=True)
    Fecha_Prestamo = models.DateField()
    Fecha_Devolucion = models.DateField()
    Observacion = models.CharField(max_length=255, null=True, blank=True)

    estudiante = models.ForeignKey(
        Estudiante,
        on_delete=models.CASCADE,
        related_name='prestamos'
    )

    libro = models.ForeignKey(
        Libro,
        on_delete=models.CASCADE,
        related_name='prestamos'
    )

    def __str__(self):
        return f"Préstamo {self.id_Prestamo}"