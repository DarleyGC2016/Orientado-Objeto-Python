from validacao import Validacao

class Servico:
    def showPrime(array):
        number = 0
        ePrimo = 0
        qtdDivisivel = 0
        print('Number  Status')
        for i in range(0, array.size()):
           number = array.get(i)
           qtdDivisivel = Validacao.validaPrimo(number, ePrimo, qtdDivisivel, array, i) 
        #    for j in range(1, number + 1 ):
        #        if number % j == 0:
        #            ePrimo+= 1
        #            qtdDivisivel = ePrimo
        #        if j ==  array.get(i): 
        #            ePrimo = 0
           if qtdDivisivel == 2:
               print(number, '      is prime')
           else:
               print(number, '      is not a prime')