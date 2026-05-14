print("=== CALCULADORA CTWMI82 EM PYTHON ===")

escolha = int(input("Digite uma das opções de operação abaixo: \n1 - Adição\n2 - Subtração\n3 - Multiplicação\n4 - Divisão\nUsuário, digite a sua escolha: "))
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

match escolha:
    case 1:
        adicao(numero1, numero2)
    case 2:
        subtracao(numero1, numero2)
    case 3:
        multiplicacao(numero1, numero2)
    case 4:
        divisao(numero1, numero2)
    case _: 
        print("Opção de operação")
    


def adicao(num1, num2):
    resultado = num1 + num2
    return resultado

def subtracao(num1, num2):
    resultado = num1 - num2
    return resultado

def multiplicacao(num1, num2):
    resultado = num1 * num2
    return resultado

def divisao(num1, num2):
    resultado = num1 / num2
    return resultado