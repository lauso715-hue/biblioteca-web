from django.db import models

class Tema(models.Model):
    Id_Tema = models.AutoField(primary_key=True)
    Nombre_Tema = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.Nombre_Tema

class Editorial(models.Model):
    Id_Editorial = models.AutoField(primary_key=True)
    Nombre_Editorial = models.CharField(max_length=100)
    Direccion = models.CharField(max_length=255)

    def __str__(self):
        return self.Nombre_Editorial

class Persona(models.Model):
    ROL_CHOICES = [
        ("Estudiante", "Estudiante"),
        ("Autor", "Autor"),
    ]
    TIPO_DOCUMENTO_CHOICES = [
        ("Cédula de Ciudadania", "Cédula de Ciudadania"),
        ("Cédula Extranjer", "Cédula Extranjer"),
        ("Tarjeta de Identidad", "Tarjeta de Identidad"),
        ("Pasaporte", "Pasaporte"),
        ("Número de Identificación", "Número de Identificación"),
    ]
    GENERO_CHOICES = [
        ("Masculino", "Masculino"),
        ("Femenino", "Femenino"),
        ("Otro", "Otro"),
    ]
    ESTADO_CHOICES = [
        ("Pendiente", "Pendiente"),
        ("Aprobado", "Aprobado"),
    ]

    Num_Documento = models.CharField(max_length=20, primary_key=True)
    Tipo_Documento = models.CharField(max_length=30, choices=TIPO_DOCUMENTO_CHOICES)
    Nombre = models.CharField(max_length=50)
    Apellido = models.CharField(max_length=50)
    Correo = models.EmailField(max_length=100, unique=True)
    Telefono = models.CharField(max_length=20)
    Fecha_Nacimiento = models.DateField()
    Genero = models.CharField(max_length=20, choices=GENERO_CHOICES)
    Rol = models.CharField(max_length=15, choices=ROL_CHOICES)
    
    # Campos para el LOGIN y APROBACIÓN (Según pizarra)
    usuario = models.CharField(max_length=50, unique=True, null=True, blank=True)
    contrasena = models.CharField(max_length=50, null=True, blank=True)
    estado = models.CharField(max_length=15, choices=ESTADO_CHOICES, default="Pendiente")

    def __str__(self):
        return f"{self.Nombre} {self.Apellido}"

class Estudiante(Persona):
    Direccion = models.CharField(max_length=150)
    Grado_Escolar = models.CharField(max_length=50)

class Autor(Persona):
    ESTADO_CHOICES = [
        ("Activo", "Activo"),
        ("Inactivo", "Inactivo"),
    ]
    Nacionalidad = models.CharField(max_length=50)
    Biografia = models.TextField(blank=True, null=True)
    Estado = models.CharField(max_length=10, choices=ESTADO_CHOICES, default="Activo")

class Libro(models.Model):
    ESTADO_CHOICES = [("Activo", "Activo"), ("Inactivo", "Inactivo")]
    Id_Libro = models.AutoField(primary_key=True)
    Titulo = models.CharField(max_length=200)
    Codigo_Barras = models.CharField(max_length=50, unique=True)
    Estado = models.CharField(max_length=10, choices=ESTADO_CHOICES, default="Activo")
    Ubicacion = models.CharField(max_length=100)
    Precio = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.Titulo

class Prestamo(models.Model):
    Id_Prestamo = models.AutoField(primary_key=True)
    Fecha_Prestamo = models.DateField(auto_now_add=True)
    Fecha_Devolucion = models.DateField()
    Observacion = models.TextField(blank=True, null=True)
    Id_Libro = models.ForeignKey(Libro, on_delete=models.CASCADE)
    Num_Documento = models.ForeignKey(Estudiante, on_delete=models.CASCADE)

class Publicacion(models.Model):
    Id_Publicacion = models.AutoField(primary_key=True)
    Descripcion = models.TextField(blank=True, null=True)
    Edicion = models.CharField(max_length=50)
    Fecha_Publicacion = models.DateField()
    ISBN = models.CharField(max_length=20, unique=True)
    Id_Libro = models.ForeignKey(Libro, on_delete=models.CASCADE)
    Id_Editorial = models.ForeignKey(Editorial, on_delete=models.CASCADE)
    Id_Tema = models.ForeignKey(Tema, on_delete=models.CASCADE)
    Num_Documento = models.ForeignKey(Autor, on_delete=models.CASCADE)