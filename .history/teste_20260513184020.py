print("=== CALCULADORA CTWMI82 EM PYTHON ===")

escolha = int(input("Digite uma das opções de operação abaixo: \n1 - Adição\n2 - Subtração\n3 - Multiplicação\n4 - Divisão\nUsuário, digite a sua escolha: "))
numero1 = float(input("Digite o primeiro número: "))
match escolha:
    case 1:
        adicao()
    case 2:
        subtracao()
    case 3:
        multiplicacao()
    case 4:
        divisao()
    case _: 
        print("Opção de operação")