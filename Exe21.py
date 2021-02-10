n1 = int(input("Digite um numero: "))
n2 = int(input("Digite outro numero: "))
contador = 0
soma = 0
mult = 1

if(n1 > n2):

    contador = n2

    while(n1 >= contador):

        if(contador % 2 == 0):

            soma = soma + contador
            contador = contador + 1

        else:
            mult = mult * contador
            contador = contador + 1


    print(soma)
    print(mult)

elif (n2 > n1):

        contador = n1

        while (n2 >= contador):

            if (contador % 2 == 0):
                soma += contador
                contador += 1
            else:
                mult *= contador
                contador += 1

        print(soma)
        print(mult)


else:
    print("Deu ruim")




