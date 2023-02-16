from django.test import TestCase


# Create your tests here.
from cafe.models import Cafe


class CafeTests(TestCase):
    """En esta clase van todas las pruebas del modelo Curso."""
    
    
    def test_largo_del_tipo(self):
        """
        Prueba crear cursos con nombres cortos y largos
        """
        tipo_nombre_valido = Cafe.objects.create(
            tipo="nombre corto", tipo=101
        )
        # Compruebo que el curso fue creado
        self.assertEqual(Cafe.objects.all().count(), 1)
        self.assertIsNotNone(cafe_tipo_valido.id)