from django.test import TestCase
from django.urls import reverse

from .models import Categoria


class CategoriaViewTests(TestCase):
    def test_inicio_muestra_las_categorias(self):
        Categoria.objects.create(nombre='Ficción', descripcion='Libros narrativos')

        response = self.client.get(reverse('catalogo:inicio'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Ficción')
        self.assertContains(response, 'Libros narrativos')
