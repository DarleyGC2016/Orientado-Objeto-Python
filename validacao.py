
class Validacao:
    # @staticmethod é usado para funções estáticas
    @staticmethod
    def validaIntAdd(array) -> None:
        while True:
            number = int(input('Número: '))
            if (number <= 1):
                break;
            else:
                array.add(number)
    
    @staticmethod
    def validaPrimo(number, ePrimo, qtdDivisivel, array, i) -> int:
        for j in range(1, number + 1 ):
            if number % j == 0:
                ePrimo+= 1
                qtdDivisivel = ePrimo
            if j ==  array.get(i): 
                ePrimo = 0            
        return qtdDivisivel