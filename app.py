from flask import Flask
import abc
from unittest import TestCase, main 

app = Flask(__name__)

class Calculadora(object):
    def calcular(self, valor1, valor2, operador):
        operacaoFabrica = OperacaoFabrica()
        operacao = operacaoFabrica.criar(operador)
        if(operacao == None):
            return 0
        else:
            resultado = operacao.executar(valor1, valor2)
            return resultado

class OperacaoFabrica():
    def criar(self, operador):
        if(operador == 'soma'):
            return Soma()
        elif(operador == 'subtracao'):
            return Subtracao()
        elif(operador == 'multiplicacao'):
            return Multiplicacao()
        elif(operador == 'divisao'):
            return Divisao()

class Operacao(metaclass = abc.ABCMeta):
    @abc.abstractmethod
    def executar(self, valor1, valor2):
        pass

class Soma(Operacao):
    def executar(self, valor1, valor2):
        resultado = valor1 + valor2
        return resultado
    
class Subtracao(Operacao):
    def executar(self, valor1, valor2):
        resultado = valor1 - valor2
        return resultado 
    
class Multiplicacao(Operacao):
    def executar(self, valor1, valor2):
        resultado = valor1 * valor2
        return resultado 
    
class Divisao(Operacao):
    def executar(self, valor1, valor2):
        resultado = valor1 / valor2
        return resultado

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
    
class Main(object):
    calculadora = Calculadora()
    x = calculadora.calcular(2, 3, 'soma')

if __name__ == "__main__":
    main()
