import random
import os

def main():
    opcao = 1

    while opcao != 2:
        print("+-------Gerador de dados-------+", " ", "      1 - Rolar", " ", "      2 - Fim", " ", "+------------------------------+", sep="\n")
        opcao = get_opcao(' ')
        if opcao == 1:
            os.system('cls' if os.name == 'nt' else 'clear')
            rolagem(opcao)
        else : 
            os.system('cls' if os.name == 'nt' else 'clear')
            print('Até mais!')
        

def get_opcao(message):
    numero = int(input(message))

    return numero


def random_number(tipodado):
    return random.randint(1, tipodado)



def rolagem(opcao):
    tipodado = get_opcao('Qual dado você escolherá? : ')
    numdados = get_opcao('Quantos você jogará?      : ')
    contagem = 0
    resultado = 0
    resultadoformatado = ''
    adicional = 0
    
    while contagem < numdados :
        adicional = get_opcao('Terá algum adicional? : ')
        randomnum = random_number(tipodado)
        resultado = randomnum + adicional
        if (contagem + 1) < numdados :
            resultadoformatado += str(resultado) + ', '
        elif (contagem + 1) == numdados :
            resultadoformatado += str(resultado) 
        contagem += 1
    os.system('cls' if os.name == 'nt' else 'clear')

    print(resultadoformatado)
    input("ENTER para continuar... ")
    os.system('cls' if os.name == 'nt' else 'clear')

    


main()
