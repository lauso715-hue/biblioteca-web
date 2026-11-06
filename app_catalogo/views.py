from django.shortcuts import render, redirect, get_object_or_404
from .models import Libro, Persona, Autor, Estudiante

def lista_libros(request):
    libros = Libro.objects.all()
    return render(request, 'inicio.html', {'libros': libros})

# 1. REGISTRAR PERSONA
def registrar_persona(request):
    if request.method == 'POST':
        Persona.objects.create(
            Num_Documento=request.POST.get('numero_documento'),
            Tipo_Documento=request.POST.get('tipo_documento'),
            Nombre=request.POST.get('nombre'),
            Apellido=request.POST.get('apellido'),
            Correo=request.POST.get('correo'),
            Telefono=request.POST.get('telefono'),
            Fecha_Nacimiento=request.POST.get('fecha_nacimiento'),
            Genero=request.POST.get('genero'),
            Rol=request.POST.get('rol'),
            usuario=request.POST.get('usuario'),
            contrasena=request.POST.get('contrasena'),
            estado="Pendiente" # Queda pendiente para que el Admin lo apruebe
        )
        # Lo enviamos a consultar para que vea que quedó pendiente
        return redirect('catalogo:consultar_persona')

    return render(request, 'registrar_persona.html')

# 2. CONSULTAR PERSONA (Buscar por ID/Documento)
def consultar_persona(request):
    persona = None
    busqueda = request.GET.get('documento', '')
    
    if busqueda:
        persona = Persona.objects.filter(Num_Documento=busqueda).first()
        
    return render(request, 'consultar.html', {'persona': persona, 'busqueda': busqueda})

# 3. COMPLETAR REGISTRO (El condicional IF)
def completar_registro(request, documento):
    persona = get_object_or_404(Persona, Num_Documento=documento)
    
    # Si no está aprobado, no lo dejamos pasar
    if persona.estado != "Aprobado":
        return redirect('catalogo:consultar_persona')

    if request.method == 'POST':
        if persona.Rol == 'Autor':
            Autor.objects.create(
                persona_ptr=persona,
                Nacionalidad=request.POST.get('nacionalidad'),
                Biografia=request.POST.get('biografia'),
                Estado="Activo"
            )
        elif persona.Rol == 'Estudiante':
            Estudiante.objects.create(
                persona_ptr=persona,
                Direccion=request.POST.get('direccion'),
                Grado_Escolar=request.POST.get('grado_escolar')
            )
        
        # Al completar, lo enviamos al Login
        return redirect('catalogo:login')

    return render(request, 'completar_registro.html', {'persona': persona})

# 4. LOGIN (Validación con sesiones de Django)
def login_view(request):
    if request.method == 'POST':
        u = request.POST.get('usuario')
        c = request.POST.get('contrasena')
        
        # Buscamos si el usuario y contraseña existen
        persona = Persona.objects.filter(usuario=u, contrasena=c).first()
        
        if persona:
            if persona.estado == 'Aprobado':
                # Creamos la sesión
                request.session['usuario_id'] = persona.Num_Documento
                request.session['usuario_nombre'] = f"{persona.Nombre} {persona.Apellido}"
                request.session['usuario_rol'] = persona.Rol
                return redirect('catalogo:inicio')
            else:
                return render(request, 'login.html', {'error': 'Tu cuenta está Pendiente de aprobación por el administrador.'})
        else:
            return render(request, 'login.html', {'error': 'Usuario o contraseña incorrectos.'})
            
    return render(request, 'login.html')

# 5. LOGOUT
def logout_view(request):
    request.session.flush() # Borra la sesión
    return redirect('catalogo:inicio')