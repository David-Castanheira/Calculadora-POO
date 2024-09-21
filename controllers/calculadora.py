from flask import Flask
import abc

app = Flask(__name__)

# Criação da classe Calculadora recebendo 3 parâmetros de entrada
class Calculadora(object):
    def calcular(self, valor1, valor2, operador):
        operacaoFabrica = OperacaoFabrica()
        operacao = operacaoFabrica.criar(operador)
        if(operacao == None):
            return 0
        else:
            resultado = operacao.executar(valor1, valor2)
            return resultado

# Criação da classe de operação utilizando-se o padrão de projeto Strategy
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

# Criação da classe abstrata
class Operacao(metaclass = abc.ABCMeta):
    @abc.abstractmethod
    def executar(self, valor1, valor2):
        if valor1 < 0 and valor2 < 0:
            raise ValueError('Essa calculadora só aceita números naturais')
        elif type(valor1) != float and type(valor1) != int: 
            raise TypeError()
        elif type(valor2) != float and type(valor2) != int:
            raise TypeError()

# Classe de soma entre dois valores
class Soma(Operacao):
    def executar(self, valor1, valor2):
        resultado = valor1 + valor2
        return resultado

# Classe de subtração entre dois valores
class Subtracao(Operacao):
    def executar(self, valor1, valor2):
        resultado = valor1 - valor2
        return resultado 

# Classe de multiplicação entre dois valores
class Multiplicacao(Operacao):
    def executar(self, valor1, valor2):
        resultado = valor1 * valor2
        return resultado 

# Classe de divisão entre dois valores   
class Divisao(Operacao):
    def executar(self, valor1, valor2):
        resultado = valor1 / valor2
        return resultado