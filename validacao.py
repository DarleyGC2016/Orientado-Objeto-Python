
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

    # Objetivo: Valida e verifica a quantidade de divisores que o número possui para se o. 
    # número é primo ou não
    # Entrada: number que será verifica se é primo ou não,
    #  ePrimo conta a quantidade de divisão tem o número,
    #  qtdDivisivel guarda quantidade exata dos divisores do número,
    # array dos números que serão verificados, i é posição da lista.
    # Saída: qtdDivisivel
    @staticmethod
    def validaPrimo(number, ePrimo, qtdDivisivel, array, i) -> int:
        for j in range(1, number + 1 ):
            if number % j == 0:
                ePrimo+= 1
                qtdDivisivel = ePrimo
            if j ==  array.get(i): 
                ePrimo = 0            
        return qtdDivisivel