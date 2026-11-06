from django.urls import path
from . import views

app_name = 'catalogo'

urlpatterns = [
    path('', views.lista_libros, name='inicio'),     
    path('lista_libros/', views.lista_libros, name='lista_libros'),
    
    # Rutas de la pizarra
    path('registrar/', views.registrar_persona, name='registrar_persona'),
    path('consultar/', views.consultar_persona, name='consultar_persona'),
    path('completar/<str:documento>/', views.completar_registro, name='completar_registro'),
    
    # Login y Logout
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]