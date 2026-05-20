def adicao(num1, num2):
    return num1 + num2

def subtracao(num1, num2):
    return num1 - num2

def multiplicacao(num1, num2):
    return num1 * num2

def divisao(num1, num2):
    return num1 / num2

def potenciacao(num1, num2):
    return num1 ** num2;

print("=== CALCULADORA CTWMI82 EM PYTHON ===")

escolha = int(input("Digite uma das opções de operação abaixo: \n1 - Adição\n2 - Subtração\n3 - Multiplicação\n4 - Divisão\n5 - Potenciação\nUsuário, digite a sua escolha: "))
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

valor = 0

match escolha:
    case 1:
        valor = adicao(numero1, numero2)
    case 2:
        valor = subtracao(numero1, numero2)
    case 3:
        valor = multiplicacao(numero1, numero2)
    case 4:
        valor = divisao(numero1, numero2)
    case 5:
        valor = 
    case _: 
        print("Opção de operação INVÁLIDA")

if escolha >= 1 and escolha <= 4:
    print("O resultado da operação é: " + str(valor))