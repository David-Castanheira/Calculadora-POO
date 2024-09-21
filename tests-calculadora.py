from unittest import TestCase, main 
from controllers.calculadora import Calculadora

class Testes(TestCase):
    def test_soma(self):
        calculadora = Calculadora()
        self.assertEqual(calculadora.calcular(2, 2, 'soma'), 4) 

    def test_subtracao(self):
        calculadora = Calculadora()
        self.assertEqual(calculadora.calcular(10, 5, 'subtracao'), 5)

    def test_multiplicacao(self):
        calculadora = Calculadora()
        self.assertEqual(calculadora.calcular(3, 3, 'multiplicacao'), 9)

    def test_divisao(self):
        calculadora = Calculadora()
        self.assertEqual(calculadora.calcular(4, 2, 'divisao'), 2)

    def test_none(self):
        calculadora = Calculadora()
        self.assertEqual(calculadora.calcular(3, 5, 'subtrair'), 0)

    def test_value_error(self):
        calculadora = Calculadora()
        assert ValueError, calculadora.calcular(-1, 1, 'soma')

    def test_type_error(self):
        calculadora = Calculadora()
        with self.assertRaises(TypeError):
            calculadora.calcular('uma', 1, 'soma')

class Main(object):
    calculadora = Calculadora()
    x = calculadora.calcular(2, 3, 'soma')

if __name__ == "__main__":
    main()