op = 0
resultado = 0
while(op!=5):
    op = int(input("Digite \n 1 para adição \n 2 para subtração \n 3 para multiplicação \n 4 para divisão \n 5 para sair. \n"))
    if(op < 5 and op > 0):
        n1 = int(input("Digite o numero 1: "))
        n2 = int(input("Digite o numero 2: "))
        if(op == 1):
            resultado = n1 + n2
        elif(op == 2):
            resultado = n1 - n2
        elif(op == 3):
            resultado = n1 * n2
        else:
            if(n1 == 0 or n2 == 0):
                print("Não pode divisão por 0")
                resultado = 0
            else:
                resultado = n1 / n2
        print("O resultado é: {} \n".format(resultado))


