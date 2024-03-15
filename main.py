import os
from myArray import MyArray
from servico import Servico
from validacao import Validacao

array = MyArray()

# valida e adiciona um número ou vários até digitar 0 ou 1
Validacao.validaIntAdd(array)

# limpa a console do windows ou do ios ou do linux
os.system('cls' if os.name == 'nt' else 'clear')

lista = Servico.verificaPrime(array)

# Apresenta os números se são número primos ou não. 
lista.sort('nro')
Servico.showPrime(lista.list)

