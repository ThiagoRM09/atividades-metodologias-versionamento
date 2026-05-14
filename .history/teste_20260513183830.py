print("=== CALCULADORA CTWMI82 EM PYTHON ===")

escolha = int(input("Digite uma das opções de operação abaixo: \n1 - Adição\n2 - Subtração\n3 - Multiplicação\n4 - Divisão\nUsuário, digite a sua escolha: "))

match escolha:
    case 1:
        adicao()
    case 2:
        subtracao()
    case 3:
        multiplicacao()
    case 4:
        
    case _: 