from django.urls import path
from . import views

app_name = 'catalogo'

urlpatterns = [
    path('', views.bienvenida, name='bienvenida'),
    path('inicio/', views.inicio, name='inicio'),
    path('despedida/', views.despedida, name='despedida'),
]