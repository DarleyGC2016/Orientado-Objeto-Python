from validacao import Validacao
from myArray import MyArray
class Servico:
    @staticmethod
    def verificaPrime(array) -> list:
        number = 0
        ePrimo = 0
        qtdDivisivel = 0
        listaNros = MyArray()

        for i in range(0, array.size()):
           number = array.get(i)
           qtdDivisivel = Validacao.validaPrimo(
                                                    number,
                                                    ePrimo,
                                                    qtdDivisivel,
                                                    array,
                                                    i
                                                ) 
           if qtdDivisivel == 2:
               listaNros.add({'nro': number, 'status': 'is prime'})
           else:
               listaNros.add({'nro': number, 'status': 'is not a prime'})
        return listaNros

    
    @staticmethod
    def showPrime(listaNros):        
        print('Number  Status')
        for lista in listaNros:
            print(str(lista['nro']),'       ',lista['status'] )
