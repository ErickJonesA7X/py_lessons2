from Estudo_Orientação_a_Objetos.calculadora import calculadora

from unittest import TestCase


class CalculadoraTest(TestCase):
    def test_soma(self):
        self.assertEqual(4, calculadora.soma(2, 2))
    def test_soma2(self):
        self.assertEqual(6, calculadora.soma(3, 3))

